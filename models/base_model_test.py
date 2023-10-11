#!/usr/bin/python3

"""
test cases for the BaseModel class
from /models/base_model.py

Unittest cases:
    TestBaseModel_instances_created
"""

import os
from datetime import datetime
from base_model import BaseModel
from time import sleep
import unittest


class TestBaseModel_instances_created(unittest.TestCase):
    """
    defines unittests for /models/base_model.py
    """

    def test_base_model_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_base_model_id_is_str(self):
        bm = BaseModel()

        self.assertEqual(str, type(bm.id))

    def test_base_model_uniq_id_instances(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        
        self.assertNotEqual(bm1.id, bm2.id)

    def test_base_model_created_at_is_datetime(self):
        bm = BaseModel()

        self.assertEqual(datetime, type(bm.created_at))

    def  test_base_model_updated_at_is_datetime(self):
        bm = BaseModel()

        self.assertEqual(datetime, type(bm.updated_at))

    def test_base_model_save(self):
        bm = BaseModel()

        bm.save()
        self.assertLess(bm.created_at, bm.updated_at)

if __name__ == "__main__":
    unittest.main()
