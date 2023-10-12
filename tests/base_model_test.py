#!/usr/bin/python3

"""
test cases for the BaseModel class
from /models/base_model.py

Unittest cases:
    TestBaseModel_instances_created
"""

import os
from datetime import datetime
from ..models.base_model import BaseModel
from time import sleep
import unittest


class TestBaseModel_instances_created(unittest.TestCase):
    """
    defines unittests for /models/base_model.py
    """

    def test_base_model_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))


if __name__ == "__main__":
    unittest.main()
