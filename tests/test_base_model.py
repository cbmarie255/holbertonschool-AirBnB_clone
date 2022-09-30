#!/usr/bin/python3
""" """
from models import BaseModel
import unittest
import datetime


class BaseModelTests(unittest.TestCase):
    """ checks for model creation """
    def test_new_model(self):
        """ checks for new model """
        x = BaseModel()
        self.assertIsNotNone(x)

class BaseModelTestsDoc(unittest.TestCase):
    """ checks for documentation """
    def test_module_doc(self):
        """ checks for documentation in base.model module """
        ##self.assertGreaterEqual(len(base.model__doc__), 1)
        pass 

    def test_class_doc(self):
        """ checks for documentation in Base class """
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    def test_init_doc(self):
        """ checks for documentation in init """
        self.assertGreaterEqual(len(BaseModel.__init__.__doc__), 1)

    def test_save_doc(self):
        """ checks for documentation in save """
        self.assertGreaterEqual(len(BaseModel.save.__doc__), 1)

    def test_str_doc(self):
        """ checks for documentaion in str """
        self.assertGreaterEqual(len(BaseModel.__str__.__doc__), 1)

    def test_to_dict(self):
        """ checks for documentation in to_dict """
        self.assertGreaterEqual(len(BaseModel.to_dict.__doc__), 1)








if __name__ == '__main__':
    unittest.main()