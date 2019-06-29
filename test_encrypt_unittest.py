import unittest
from vigenere import *


class TestEncrypt(unittest.TestCase):

    def setUp(self):
        pass
    #Test a long message
    def test_ENC_long(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        message = 'DEFENDTHEEASTWALLOFTHECASTLE'
        key = 'FORTIFICATION'
        self.assertEqual( encrypt(key,message,table,0), 'ISWXVIBJEXIGGBOCEWKBJEVIGGQS')

    #Test a single character message
    def test_ENC_single(self):
        tables = createTables(list('TEST'))
        table = tables[0]
        message = 'N'
        key = 'I'
        self.assertEqual( encrypt(key,message,table,0), 'V')


if __name__ == '__main__':
    unittest.main()
