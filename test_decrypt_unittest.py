import unittest
from vigenere import *


class TestDecrypt(unittest.TestCase):

    def setUp(self):
        pass
    #Test a long message
    def test_DEC_long(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        message = 'ISWXVIBJEXIGGBOCEWKBJEVIGGQS'
        key = 'FORTIFICATION'
        self.assertEqual( decrypt(key,message,table,0), 'DEFENDTHEEASTWALLOFTHECASTLE')

    #Test a single character message
    def test_DEC_single(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        message = 'V'
        key = 'I'
        self.assertEqual( decrypt(key,message,table,0),'N' )

    def test_DEC_single(self):
        tables = createTables(list('TEST'))
        table = tables[1]
        message = 'I'
        key = 'F'
        self.assertEqual( decrypt(key,message,table,0),'D' )


if __name__ == '__main__':
    unittest.main()
