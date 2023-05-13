#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_attributes(self):
        """Test that City has the required attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
