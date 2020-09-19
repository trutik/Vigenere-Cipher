from unittest import TestCase, main
from vigenere import createTables, decrypt

class TestDecrypt(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Using setUpClass to generate data sets only once, as they will be re-used across all tests. """
        tables = createTables(list('TEST'))
        cls.encryption_table = tables[0]
        cls.decryption_table = tables[1]

    def _test_decrypt_message(self,message,key,expected_output):
        decrypted_message = decrypt(key, message, self.decryption_table, 0)
        self.assertEqual(decrypted_message, expected_output)

    def test_decryption_long_message(self):
        """ Test decryption of a relatively long message. """
        self._test_decrypt_message('ISWXVIBJEXIGGBOCEWKBJEVIGGQS','FORTIFICATION','DEFENDTHEEASTWALLOFTHECASTLE')

    def test_decryption_single_char(self):
        """ Test decryption of a single character message. """
        self._test_decrypt_message('V','I','N')

    def test_decryption_single_char_2(self):
        """ Test decryption of a single character message. """
        self._test_decrypt_message('I', 'F', 'D')


if __name__ == '__main__':
    main()
