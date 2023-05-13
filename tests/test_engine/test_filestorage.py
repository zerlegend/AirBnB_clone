#!/usr/bin/python3
"""Test the FileStorage class."""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def setUp(self):
        """Create a new instance of FileStorage."""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all() method."""
        # Create some objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        # Add them to the storage
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        # Make sure they're all in the all() dictionary
        self.assertIn("BaseModel.{}".format(obj1.id), self.storage.all())
        self.assertIn("User.{}".format(obj2.id), self.storage.all())
        self.assertIn("State.{}".format(obj3.id), self.storage.all())

    def test_new(self):
        """Test the new() method."""
        # Create an object and add it to the storage
        obj = BaseModel()
        self.storage.new(obj)
        # Make sure it's in the storage dictionary
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """Test the save() method."""
        # Create some objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        # Add them to the storage
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        # Save the storage to a file
        self.storage.save()
        # Make sure the file was created
        with open(self.storage._FileStorage__file_path, 'r') as f:
            self.assertTrue(len(f.read()) > 0)

    def test_reload(self):
        """Test the reload() method."""
        # Create some objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        # Add them to the storage and save the storage to a file
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()
        # Clear the storage dictionary
        self.storage._FileStorage__objects = {}
        # Reload the storage from the file
        self.storage.reload()
        # Make sure the objects are in the all() dictionary
        self.assertIn("BaseModel.{}".format(obj1.id), self.storage.all())
        self.assertIn("User.{}".format(obj2.id), self.storage.all())
        self.assertIn("State.{}".format(obj3.id), self.storage.all())


if __name__ == "__main__":
    unittest.main()
