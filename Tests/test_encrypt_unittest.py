from unittest import TestCase, main
from vigenere import create_tables, encrypt
from utilities import base_encrypt_decrypt_test


class TestEncrypt(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Using setUpClass to generate data sets only once, as they will be re-used across all tests. """
        tables = create_tables(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        cls.encryption_table = tables[0]

    #Test a long message
    def test_ENC_long(self):
        base_encrypt_decrypt_test(self, encrypt,
                                  'DEFENDTHEEASTWALLOFTHECASTLE', 'FORTIFICATION', 'ISWXVIBJEXIGGBOCEWKBJEVIGGQS')

    #Test a single character message
    def test_ENC_single(self):
        base_encrypt_decrypt_test(self, encrypt,'N', 'I', 'V')


if __name__ == '__main__':
   main()
