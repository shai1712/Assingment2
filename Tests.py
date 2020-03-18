import unittest
from Quotes import BrakingBad


class BreakingBadTest(unittest.TestCase):

    def test_get_list_quotes(self):

        # assume
        stub1 = -1
        stub2 = 0

        # expected
        expected1 = []
        expected2 = []

        quote_result1 = BrakingBad.list_quotes(stub1)
        quote_result2 = BrakingBad.list_quotes(stub2)

        # assert
        self.assertEqual(quote_result1, expected1)
        self.assertEqual(quote_result2, expected2)


    def test_get_random_quote(self):

        # expected
        expected = ""

        # action
        quote_result = BrakingBad.quote()

        # assert
        #self.assertEqual(quote_result, expected)


if __name__ == '__main__':
    unittest.main()