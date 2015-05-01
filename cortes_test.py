# coding=utf8

import unittest
import cortes

class BasicTestCase(unittest.TestCase):
    def testIdentifier(self):
        self.assertEqual(
            str(cortes.extract(["bar"], (0, 1))),
            "[bar]"
        )

    def testIdentifierWithSpaces(self):
        self.assertEqual(
            str(cortes.extract([" bar "], (0, 1))),
            " [bar] "
        )

    def testTwoIdentifiers(self):
        self.assertEqual(
            str(cortes.extract(["bar baz"], (0, 1))),
            "[[bar] [baz]]"
        )


if __name__ == '__main__':
	unittest.main()
