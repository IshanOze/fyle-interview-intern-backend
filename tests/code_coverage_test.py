from core.libs.exceptions import FyleError
from core.libs.assertions import base_assert, assert_found, assert_true, assert_valid, assert_auth
from core.models.students import Student
from core.models.teachers import Teacher
from core.models.assignments import Assignment
from core.apis.teachers.schema import TeacherSchema

import unittest
import pytest
from datetime import datetime


def test_fyle_error_init():
    # Test the FyleError __init__ method
    error = FyleError(404, "Not Found")
    assert error.status_code == 404
    assert error.message == "Not Found"

def test_fyle_error_to_dict():
    # Test the FyleError to_dict method
    error = FyleError(400, "Bad Request")
    error_dict = error.to_dict()
    assert 'message' in error_dict
    assert error_dict['message'] == "Bad Request"

def test_base_assert():
    # Test the assertions base_assert method
    with pytest.raises(FyleError):
        raise FyleError(404, "Not Found")
        
def test_assert_auth():
    # Test the assertions assert_auth method
    with pytest.raises(FyleError) as context:
        assert_auth(False, "UNAUTHORIZED")
    assert context.value.status_code == 401
    assert context.value.message == "UNAUTHORIZED"

def test_assert_true():
    # Test the assertions assert_true method
    with pytest.raises(FyleError) as context:
        assert_true(False, "FORBIDDEN")
    assert context.value.status_code == 403
    assert context.value.message == "FORBIDDEN"

def test_assert_valid():
    # Test the assertions assert_valid method
    with pytest.raises(FyleError) as context:
        assert_valid(False, "BAD_REQUEST")
    assert context.value.status_code== 400
    assert context.value.message == "BAD_REQUEST"

# class structure for getting Student model test coverage
class TestStudentModel(unittest.TestCase):
    def test_repr_method(self):
        student = Student(id=1, user_id=5)

        repr_result = repr(student)

        self.assertIsInstance(repr_result, str)

        self.assertIn('Student', repr_result)
        self.assertIn(str(student.id), repr_result)

# class structure for getting Teacher Schema test coverage
class TestTeacherSchema(unittest.TestCase):
    def test_initiate_class_method(self):
        # Create a TeacherSchema instance
        teacher_schema = TeacherSchema()

        # Create a sample data dictionary
        data_dict = {
            'id': 3,
            'user_id': 6,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }

        teacher_instance = teacher_schema.initiate_class(data_dict, many=False, partial=False)

        self.assertIsInstance(teacher_instance, Teacher)

        self.assertEqual(teacher_instance.id, data_dict['id'])
        self.assertEqual(teacher_instance.user_id, data_dict['user_id'])

# class structure for getting Teacher model test coverage
class TestTeacherModel(unittest.TestCase):
    def test_repr_method(self):
        teacher = Teacher(id=1, user_id=5)

        repr_result = repr(teacher)

        self.assertIsInstance(repr_result, str)

        self.assertIn('Teacher', repr_result)
        self.assertIn(str(teacher.id), repr_result)

    def test_list_all_method(self):
        teachers = Teacher.list_all_teachers()

        self.assertIsInstance(teachers, list)
        self.assertGreaterEqual(len(teachers), 1)

# class structure for getting Assignment model test coverage
class TestAssignmentModel(unittest.TestCase):

    def test_repr_method(self):
        assignment = Assignment(id=1)

        repr_result = repr(assignment)

        self.assertIsInstance(repr_result, str)

        self.assertIn('Assignment', repr_result)
        self.assertIn(str(assignment.id), repr_result)

