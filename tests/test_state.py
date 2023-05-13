import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes_initialization(self):
        state = State()
        self.assertEqual(state.name, "")
