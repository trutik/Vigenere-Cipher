from unittest import TestCase, main
from vigenere import create_tables


class TestCreateTables(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Using setUpClass to generate data sets only once, as they will be re-used across all tests. """
        tables = create_tables(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        cls.encryption_table = tables[0]
        cls.decryption_table = tables[1]

    #Test each corner of the 'tabula recta' and the center, is mapping as expected?

    #Test encryption table.

    def test_createtables_encryption_top_left(self):
        self.assertEqual( self.encryption_table['AA'], 'A')

    def test_createtables_encryption_top_right(self):
        self.assertEqual( self.encryption_table['AZ'], 'Z')

    def test_createtables_encryption_center(self):
        self.assertEqual( self.encryption_table['LM'], 'X')

    def test_createtables_encryption_bottom_left(self):
        self.assertEqual( self.encryption_table['ZA'], 'Z')

    def test_createtables_encryption_bottom_right(self):
        self.assertEqual( self.encryption_table['ZZ'], 'Y')

    #Testing decryption table.

    def test_createtables_decryption_top_left(self):
        self.assertEqual( self.decryption_table['AA'], 'A')

    def test_createtables_decryption_top_right(self):
        self.assertEqual( self.decryption_table['AZ'], 'Z')

    def test_createtables_decryption_center(self):
        self.assertEqual( self.decryption_table['LX'], 'M')

    def test_createtables_decryption_bottom_left(self):
        self.assertEqual( self.decryption_table['ZZ'], 'A')

    def test_createtables_decryption_bottom_right(self):
        self.assertEqual( self.decryption_table['ZY'], 'Z')

if __name__ == '__main__':
    main()
