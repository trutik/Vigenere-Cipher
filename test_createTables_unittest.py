import unittest
from vigenere import *


class TestCreateTables(unittest.TestCase):

    def setUp(self):
        pass
    #Test each corner of the 'tabula recta' and the center, is mapping as expected?
    def test_createtablesENC_top_left(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        self.assertEqual( table['AA'], 'A')

    def test_createtablesENC_top_right(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        self.assertEqual( table['AZ'], 'Z')

    def test_createtablesENC_center(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        self.assertEqual( table['LM'], 'X')

    def test_createtablesENC_bottom_left(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        self.assertEqual( table['ZA'], 'Z')

    def test_createtablesENC_bottom_right(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        self.assertEqual( table['ZZ'], 'Y')

    ##############################
    #Test decryption table now
    def test_createtablesDEC_top_left(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        self.assertEqual( table['AA'], 'A')

    def test_createtablesDEC_top_right(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        self.assertEqual( table['AZ'], 'Z')

    def test_createtablesDEC_center(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        self.assertEqual( table['LX'], 'M')

    def test_createtablesDEC_bottom_left(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        self.assertEqual( table['ZZ'], 'A')

    def test_createtablesDEC_bottom_right(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        self.assertEqual( table['ZY'], 'Z')

if __name__ == '__main__':
    unittest.main()
