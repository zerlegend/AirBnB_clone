#!/usr/bin/python3
"""Define unit tests for the User class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Define unit tests for the User class."""

    def test_attributes(self):
        """Test that User class has email, password,
        first_name, and last_name attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_email_attribute(self):
        """Test that User class has email attribute."""
        user = User()
        self.assertEqual(user.email, "")

    def test_password_attribute(self):
        """Test that User class has password attribute."""
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_attribute(self):
        """Test that User class has first_name attribute."""
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        """Test that User class has last_name attribute."""
        user = User()
        self.assertEqual(user.last_name, "")
