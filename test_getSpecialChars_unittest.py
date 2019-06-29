import unittest
from vigenere import *


class TestGetSpecialChars(unittest.TestCase):

    def setUp(self):
        pass
    #Test no special character input
    def test_getSpecialChars_none(self):
        chars = getSpecialChars('return nothing')
        chars = ''.join(chars)
        self.assertEqual( chars, '')

    #Test single special character input
    def test_getSpecialChars_one(self):
        chars = getSpecialChars('§')
        chars = ''.join(chars)
        self.assertEqual( chars, '§')

    #Test single special character input
    def test_getSpecialChars_many(self):
        chars = getSpecialChars('§ËÞ231@#')
        chars = ''.join(chars)
        self.assertEqual( chars, '§ËÞ')


if __name__ == '__main__':
    unittest.main()
