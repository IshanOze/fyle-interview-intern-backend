from marshmallow import Schema, post_load, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unkown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    user_id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return Teacher(**data_dict)