import mysql.connector
from .utils import Field


class BaseManager:
    connection = None

    @classmethod
    def set_connection(cls, database_settings):
        connection = mysql.connector.connect(**database_settings)
        connection.autocommit = True
        cls.connection = connection

    @classmethod
    def _get_cursor(cls):
        return cls.connection.cursor()

    @classmethod
    def _execute_query(cls, query, vars):
        cursor = cls._get_cursor()
        cursor.execute(query, vars)

    def __init__(self, model_class):
        self.model_class = model_class

    @property
    def table_name(self):
        return self.model_class.table_name

    def _get_fields(self):
        cursor = self._get_cursor()
        cursor.execute(
            """
            SELECT column_name, 
                data_type FROM information_schema.columns WHERE table_name=%s
            """,
            (self.table_name, )
        )

        return [Field(name=row[0], data_type=row[1])
                for row in cursor.fetchall()]

    def select(self, *field_names, chunk_size=2000, condition=None):
        # Build SELECT query
        if '*' in field_names:
            fields_format = '*'
            field_names = [field.name for field in self._get_fields()]
        else:
            fields_format = ', '.join(field_names)

        query = f"SELECT {fields_format} FROM {self.table_name}"
        vars = []
        if condition:
            query += f" WHERE {condition.sql_format}"
            vars += condition.query_vars

        # Execute query
        cursor = self._get_cursor()
        cursor.execute(query, vars)

        # Fetch data obtained with the previous query execution and
        # transform it into `model_class` objects.
        # The fetching is done by batches to avoid to run out of memory.
        model_objects = list()
        is_fetching_completed = False
        while not is_fetching_completed:
            rows = cursor.fetchmany(size=chunk_size)
            for row in rows:
                row_data = dict(zip(field_names, row))
                model_objects.append(self.model_class(**row_data))
            is_fetching_completed = len(rows) < chunk_size

        return model_objects

    def execute_custom_query(self, query, vars=[], chunk_size=2000):
        # Execute query
        cursor = self._get_cursor()
        cursor.execute(query, vars)

        field_names = [x[0] for x in cursor.description]

        # Fetch data obtained with the previous query execution
        # and transform it into `model_class` objects.
        # The fetching is done by batches to avoid to run out of memory.
        model_objects = list()
        is_fetching_completed = False
        while not is_fetching_completed:
            rows = cursor.fetchmany(size=chunk_size)
            for row in rows:
                row_data = dict(zip(field_names, row))
                model_objects.append(self.model_class(**row_data))
            is_fetching_completed = len(rows) < chunk_size

        return model_objects

    def execute_scripts_from_file(cls, filename):
        # Open and read the file as a single buffer
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                cls._execute_query(command, [])
            except Exception as e:
                print("Command skipped: ", e)
