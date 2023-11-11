import unittest
from datetime import datetime
from models.base_model import BaseModel
import models.base_model

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_doc_module(self):
        """Test base module for documentation"""
        self.assertIsNotNone(__import__('models.base_model').__doc__)

    def test_doc_class(self):
        """Test class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_instance_attributes(self):
        """Test the presence and type of instance attributes"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_method(self):
        """Test the save method"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str_method(self):
        """Test the __str__ method"""
        obj = BaseModel()
        str_representation = str(obj)
        self.assertIsInstance(str_representation, str)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(obj.id, str_representation)



if __name__ == '__main__':
    unittest.main()
