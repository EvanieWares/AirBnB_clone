import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.obj = BaseModel()

    def test_initialization(self):
        self.assertIsNotNone(self.obj.id)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_string_representation(self):
        expected_string = f'BaseModel ({self.obj.id}) {{"id": "{self.obj.id}","created_at": "{self.obj.created_at.isoformat()}","updated_at": "{self.obj.updated_at.isoformat()}"}}'
        self.assertEqual(str(self.obj), expected_string)

    def test_to_dict_method(self):
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.obj.id)
        self.assertEqual(obj_dict['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.obj.updated_at.isoformat())

    def test_custom_attributes(self):
        obj_with_attributes = BaseModel(name='Effah', age=40)
        self.assertEqual(obj_with_attributes.name, 'Effah')
        self.assertEqual(obj_with_attributes.age, 40)

    def test_custom_attributes_to_dict(self):
        obj_with_attributes = BaseModel(name='Effah', age=40)
        obj_dict = obj_with_attributes.to_dict()
        self.assertEqual(obj_dict['name'], 'Effah')
        self.assertEqual(obj_dict['age'], 40)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            BaseModel(created_at='2023-11-09 10:30:00')

    def test_exception_handling(self):
        with self.assertRaises(AttributeError):
            obj = BaseModel(unknown_attribute='value')

    def test_persistence(self):
        # Test saving and loading objects from storage
        obj = BaseModel()
        obj_id = obj.id
        storage.new(obj)
        storage.save()
        loaded_obj = storage.all().get(f"BaseModel.{obj_id}")
        self.assertIsNotNone(loaded_obj)

    def test_concurrent_operations(self):
        # Test concurrent operations on objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_boundary_cases(self):
        obj = BaseModel(name='X' * 25, age=100)
        self.assertEqual(len(obj.name), 25)
        self.assertEqual(obj.age, 100)

if __name__ == '__main__':
    unittest.main()
