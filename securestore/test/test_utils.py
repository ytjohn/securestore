# -*- coding: utf-8 -*-
"""
    PyCharm	
    ~~~~~~

    :copyright: (c) 2011 by ytjohn
    :license: BSD, see LICENSE for more details.
"""

import unittest

class FooTests(unittest.TestCase):

    def setUp(self):
        self.stuff = 'stuff'

    def tearDown(self):
        self.stuff = None

    def testFoo(self):
        self.assertEqual('stuff', 'stuff')

    def testBar(self):
        self.assertEqual(self.stuff, 'stuff')


def main():
    unittest.main()

if __name__ == '__main__':
    main()

