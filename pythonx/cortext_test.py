# coding=utf8

import unittest
import cortex

class BasicTestCase(unittest.TestCase):
    def testIdentifier(self):
        self.assertEqual(
            str(cortex.extract(["bar"], (0, 1))),
            "[bar]"
        )

    def testIdentifierWithSpaces(self):
        self.assertEqual(
            str(cortex.extract([" bar "], (0, 1))),
            " [bar] "
        )

    def testTwoIdentifiers(self):
        self.assertEqual(
            str(cortex.extract(["bar baz"], (0, 1))),
            "[[bar] [baz]]"
        )


if __name__ == '__main__':
	unittest.main()
