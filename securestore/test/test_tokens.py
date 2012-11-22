# -*- coding: utf-8 -*-
"""
    PyCharm	
    ~~~~~~

    :copyright: (c) 2011 by ytjohn
    :license: BSD, see LICENSE for more details.
"""

import unittest
from securestore.tokens import tokens

class TokenTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.key = 't' * 32
        self.tok = tokens(':memory:', self.key)

    @classmethod
    def tearDownClass(self):
        self.key = None
        self.tok = None

    def testTableExists(self):
        # class will always generate table if it doesn't exist
        self.assertTrue(self.tok._tableexists('tokens'))

    def testMakeTableAgain(self):
        # do this twice, should fail for duplicate table
        self.assertEqual(self.tok._generatetable(), "error: table already "
                                                 "exists")

    def testAddTokens(self):
        # single bit of text
        id = self.tok.record('password')
        self.assertEqual(id, 1)
        # token with space
        id = self.tok.record('pass word')
        self.assertEqual(id, 2)
        # token with single quote
        id = self.tok.record("pass'word")
        self.assertEqual(id, 3)

    def testAddEmptyToken(self):
        # empty token should fail as False
        id = self.tok.record('')
        self.assertFalse(id)

    def testGetValidTokens(self):
        self.assertEqual(self.tok.get(1), 'password')
        self.assertEqual(self.tok.get(2), 'pass word')
        self.assertEqual(self.tok.get(3), 'pass\'word')

    def testGetInvalidToken(self):
        self.assertFalse(self.tok.get('invalid'))

    def testUpdateValidToken(self):
        id = self.tok.record('updated', 1)
        self.failUnless(id == 1)
        new = self.tok.get(1)
        self.failUnless(new == 'updated')

    def testUpdateInvalidToken(self):
        result = self.tok.record('updated2', 'invalid')
        self.assertFalse(result)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

    