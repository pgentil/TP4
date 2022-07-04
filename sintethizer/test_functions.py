#Testing python file - pytest
import unittest

import ASD_functions.functions as functions

import numpy as np

import matplotlib.pyplot as plt


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.function = functions.Function()

    def test_LINEAR(self):
        array = np.arange(0, 6, 1.)
        result = self.function.LINEAR(1, array)
        expected = np.array([0, 1, 2, 3, 4, 5])
        self.assertTrue(np.allclose(result, expected))
        pass

    def test_EXP(self):
        array = np.arange(0, 6, 1.)
        result = self.function.EXP(1, array)
        expected = np.array([(np.e)**(-5), 1.0 , (np.e)**(5), (np.e)**10, (np.e)**(15), (np.e)**(20)])
        self.assertTrue(np.allclose(result, expected))

    def test_QUARTSIN(self):
        array = np.arange(0, 6, 1.)
        result = self.function.QUARTSIN(1, array)
        expected = np.sin((np.pi * array)/2)
        self.assertTrue(np.allclose(result, expected))

    def test_HALFSIN(self):
        array = np.arange(0, 6, 1.)
        result = self.function.HALFSIN(1, array)
        expected = (1 + np.cos(np.pi * (array - 0.5))) / 2
        self.assertTrue(np.allclose(result, expected))

    def test_LOG(self):
        array = np.arange(0, 6, 1.)
        result = self.function.LOG(1, array)
        expected = np.log10(9 * array + 1)
        self.assertTrue(np.allclose(result, expected))

    def test_TRI(self):
        pass
        # array = np.arange(0, 6, 1.)
        # result = self.function.TRI(1, 3, 2, array)
        # plt.plot(array, result)
        # plt.show
        # expected = np.array([0])
        # self.assertTrue(np.allclose(result, expected))

    def test_CONSTANT(self):
        array = np.arange(0, 6, 1.)
        result = self.function.CONSTANT(array)
        expected = np.ones(len(array))
        self.assertTrue(np.allclose(result, expected))

    def test_INVLINEAR(self):
        array = np.arange(0, 2.5, .5)
        result = self.function.INVLINEAR(1, array)
        expected = np.array([1, 0.5, 0, 0, 0])
        self.assertTrue(np.allclose(result, expected))

    def test_SIN(self):
        array = np.arange(0, 2.5, .5)
        result = self.function.SIN(1, np.pi, array)
        expected = np.array([1, 2, 1, 0, 1])
        self.assertTrue(np.allclose(result, expected))

    def test_INVEXP(self):
        array = np.arange(0, 6, 1.)
        result = self.function.INVEXP(1, array)
        expected = np.array([np.e**(0), np.e**(-5), np.e**(-10), np.e**(-15), np.e**(-20), np.e**(-25)])
        self.assertTrue(np.allclose(result, expected))

    def test_QUARTCOS(self):
        array = np.arange(0, 6, 1.)
        result = self.function.QUARTCOS((1/2), array)
        expected = np.array([np.cos(0), np.cos(np.pi),np.cos(np.pi * 2), np.cos(np.pi * 3), np.cos(np.pi * 4), np.cos(np.pi * 5)])
        self.assertTrue(np.allclose(result, expected))

    def test_HALFCOS(self):
        array = np.arange(0, 6, 1.)
        result = self.function.HALFCOS(1, array)
        expected = np.array([ 1, 0, 1, 0, 1, 0])
        self.assertTrue(np.allclose(result, expected))

    def test_INVLOG(self):
        array = np.arange(0, 2.5, .5)
        result = self.function.INVLOG(1, array)
        expected = np.array([ 1, np.log10(5.5), 0, 0, 0])
        self.assertTrue(np.allclose(result, expected))

    def test_PULSES(self):
        pass
        # array = np.arange(0, 6, 1)
        # result = self.function.PULSES(1, array)
        # expected = np.array([ 1, np.log10(5.5), 0, 0, 0])
        # self.assertTrue(np.allclose(result, expected))

    def tearDown(self) -> None:
        del self.function

if __name__ == "__main__":
    unittest.main()