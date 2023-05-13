import unittest
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test fixtures."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_instantiation(self):
        """Test that a new instance of BaseModel
        has the expected attributes."""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertEqual(self.model.__class__.__name__, "BaseModel")

    def test_save(self):
        """Test that the updated_at attribute
        is updated and that save() works."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that to_dict() returns the
        expected dictionary."""
        model_dict = self.model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertTrue("id" in model_dict)
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)


if __name__ == '__main__':
    unittest.main()
