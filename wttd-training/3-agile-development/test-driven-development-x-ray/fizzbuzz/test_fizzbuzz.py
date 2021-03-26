import unittest
from fizzbuzz import robot


class FizzbuzzTest(unittest.TestCase):
    def test_say_one_when_one(self):
        self.assertEqual(robot(1), '1')
