#Testing python file - pytest
import unittest

import ASD_functions.functions as functions

import numpy as np


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.function = functions.Function()

    def test_LINEAR(self):
        array = np.arange(0, 120.5, 0.5)
        self.assertEqual(self.function.LINEAR(0.5, 60, 4), array)
        pass

    def test_EXP(self):
        pass

    def test_QUARTSIN(self):
        pass

    def test_HALFSIN(self):
        pass

    def test_LOG(self):
        pass

    def test_TRI(self):
        pass

    def test_CONSTANT(self):
        pass

    def test_INVLINEAR(self):
        pass

    def test_SIN(self):
        pass

    def test_INVEXP(self):
        pass

    def test_QUARTCOS(self):
        pass

    def test_HALFCOS(self):
        pass

    def test_INVLOG(self):
        pass

    def test_PULSES(self):
        pass

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()