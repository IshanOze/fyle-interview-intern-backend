from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema


principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns the list of all teachers"""
    
    if p.principal_id == 1:
        all_teachers = Teacher.list_all_teachers()
        all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
        return APIResponse.respond(data=all_teachers_dump)
    else:
        return APIResponse.respond(data=[])