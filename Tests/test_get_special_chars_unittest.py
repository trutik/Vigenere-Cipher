from unittest import TestCase, main
from vigenere import get_special_chars



class TestGetSpecialChars(TestCase):

    def setUp(self):
        pass
    #Test no special character input

    def _test_get_special_chars_base(self, input, expected_output):
        """ Assert the output is equal to the expected output for a given input. Base test function """
        chars = get_special_chars(input)
        chars = ''.join(chars)
        self.assertEqual(chars, expected_output)

    def test_get_special_chars_none(self):
        """ Test case of no special characters being passed. """
        self._test_get_special_chars_base('return nothing', '')

    def test_get_special_chars_one(self):
        """ Test case of a single special character as input. """
        self._test_get_special_chars_base('§', '§')

    def test_get_special_chars_multiple(self):
        """ Test case of multiple special characters as input. """
        self._test_get_special_chars_base('§ËÞ231@#', '§ËÞ')


if __name__ == '__main__':
    main()
