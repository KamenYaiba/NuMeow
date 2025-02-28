from src.config import precision
from src.helping_functions import elementary_symmetric_sum
import unittest
import math


class HelpingFunctionsTest(unittest.TestCase):
    def test_elementary_symmetric_sum(self):
        actual = elementary_symmetric_sum([1, 2, 3, 4])
        expected = [1, 10, 35, 50, 24]
        for a, e in zip(actual, expected):
            self.assertTrue(math.isclose(a, e, rel_tol=precision))

        actual = elementary_symmetric_sum([-3.33, -3.5, -4.02, -4.5084, -4.8201, -5.0801, -5.3087])
        expected = [1, -30.5673, 398.65589151, -2875.250110341287, 12384.0716941806395808, -31850.43956601236077338,
                    45286.25641960449491569728, -27458.52885732516682033548]
        for a, e in zip(actual, expected):
            self.assertTrue(math.isclose(a, e, rel_tol=precision))

