from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from project.server.models import Property

property_blueprint = Blueprint('property', __name__)


class PropertyAPI(MethodView):
    """
    Property Resource
    """

    def get(self, *args, **kwargs):
        status = request.args.get('status')
        year = request.args.get('year')
        city = request.args.get('city')
        next = request.args.get('next', 0)
        query = """
            select p.address, p.city, sh_max.status_id, p.price, 
                p.description, p.year
            from property p join 
                (select MAX(sh.update_date), sh.property_id, sh.status_id  
                    from status_history sh group by sh.property_id 
                ) as sh_max
            where p.id = sh_max.property_id 
                and sh_max.status_id in (3,4,5)
            """
        query += f" and sh_max.status_id = {status} " if status else ""
        query += f" and p.year = {year} " if year else ""
        query += f" and p.city = '{city}' " if city else ""

        query += f" LIMIT 200 OFFSET {int(next) * 200} "

        properties = Property.objects.execute_custom_query(
            query
        )
        properties_json = [ob.__dict__ for ob in properties]

        responseObject = {
            'status': 'success',
            'data': {
                'count': len(properties_json),
                'properties': properties_json,
            }
        }
        return make_response(jsonify(responseObject)), 200


# define the API resources
property_application_view = PropertyAPI.as_view('property_api')

# add Rules for API Endpoints
property_blueprint.add_url_rule(
    '/property/',
    view_func=property_application_view,
    methods=['GET']
)
