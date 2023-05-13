#!/usr/bin/python3
"""Unit tests for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    """Test cases for console.py"""
    
    def test_prompt(self):
        """Test that the prompt is (hbnb)"""
        self.assertEqual("(hbnb) ", console.HBNBCommand.prompt)
        
    def test_emptyline(self):
        """Test that an empty line does not execute"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("\n")
        self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test that quit command exits"""
        with self.assertRaises(SystemExit):
            console.HBNBCommand().onecmd("quit")

    def test_eof(self):
        """Test that EOF command exits"""
        with self.assertRaises(SystemExit):
            console.HBNBCommand().onecmd("EOF")

    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help")
        self.assertIn("Documented commands (type help <topic>):", f.getvalue())

if __name__ == '__main__':
    unittest.main()
