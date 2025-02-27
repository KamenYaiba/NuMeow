from src.interpolation import nevilles_method, nevilles_method_steps
from src.config import precision
import unittest
import math


class TestInterpolation(unittest.TestCase):
    def test_nevilles_method(self):
        test = nevilles_method([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4)
        self.assertTrue(math.isclose(test, 17.87713, rel_tol=precision))
        test = nevilles_method([8.1, 8.3], [16.94410, 17.56492, 18.50515], 8.4)
        self.assertTrue(test is False)
        test = nevilles_method([8.1, 8.3, 8.6], [], 8.4)
        self.assertTrue(test is False)
        test = nevilles_method([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828, 4.48169], 0.43)
        self.assertTrue(math.isclose(test, 2.36060473408, rel_tol=precision))

    def test_nevilles_method_steps(self):
        expected = [1, 1.64872, 2.71828, 4.48169, 2.1157984, 2.4188032, 2.2245251999999995, 2.3763825279999997, 2.34886312, 2.36060473408]
        actual = nevilles_method_steps([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828, 4.48169], 0.43)
        for e, a in zip(expected, actual):
            self.assertTrue(math.isclose(e, a, rel_tol=precision))

        expected = [16.9441, 17.56492, 18.50515, 17.875329999999998, 17.878330000000002, 17.87713]
        actual = nevilles_method_steps([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4)
        for e, a in zip(expected, actual):
            self.assertTrue(math.isclose(e, a, rel_tol=precision))

        self.assertTrue(nevilles_method_steps([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828], 0.43) is False)
        self.assertTrue(nevilles_method_steps([], [1, 1.64872, 2.71828, 4.48169], 0.43) is False)



