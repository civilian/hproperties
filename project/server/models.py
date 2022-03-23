from .orm import BaseModel, BaseManager


class Property(BaseModel):
    table_name = "property"
    manager_class = BaseManager
