import os
import unittest
from util.random_string_generator import RandomString

class TestRandomString(unittest.TestCase):

    def test_generate_six_character_long(self):
        code = RandomString.generate(6)
        self.assertEqual(len(code),6)

if __name__=='__main__':
    unittest.main()

