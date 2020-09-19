from unittest import TestCase, main
from vigenere import create_tables, decrypt
from utilities import base_encrypt_decrypt_test

class TestDecrypt(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Using setUpClass to generate data sets only once, as they will be re-used across all tests. """
        tables = create_tables(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        cls.decryption_table = tables[1]

    def test_decryption_long_message(self):
        """ Test decryption of a relatively long message. """
        base_encrypt_decrypt_test(self, decrypt,
                                 'ISWXVIBJEXIGGBOCEWKBJEVIGGQS','FORTIFICATION','DEFENDTHEEASTWALLOFTHECASTLE')

    def test_decryption_single_char(self):
        """ Test decryption of a single character message. """
        base_encrypt_decrypt_test(self, decrypt,'V','I','N')

    def test_decryption_single_char_2(self):
        """ Test decryption of a single character message. """
        base_encrypt_decrypt_test(self, decrypt,'I', 'F', 'D')


if __name__ == '__main__':
    main()
