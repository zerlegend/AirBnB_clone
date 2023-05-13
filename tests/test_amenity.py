#!/usr/bin/python3
"""Unit tests for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Define tests for Amenity class."""

    def test_attribute_type(self):
        """Test that the attributes of Amenity are strings."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")
