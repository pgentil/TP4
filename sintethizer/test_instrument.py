import unittest

import ASD_functions.instrument as instrument

from functions import Function

import numpy as np

import matplotlib.pyplot as plt

class TestInstruments(unittest.TestCase):

    def setUp(self) -> None:
        self.instrument = instrument.Instrument()
        self.function = Function()
    
    def test_read_instrument(self):
        self.instrument.read_instrument('sintethizer\ASD_functions\instruments\piano.txt')
        self.assertTrue(len(self.instrument.harmonics)==4 and len(self.instrument.functions)==3)

    def test_get_functions(self):
        param = ['TRI', '0.05', '0.03', '1.3']
        array = np.array([1,2,3,4,5])
        func = self.instrument.get_functions(param, array)
        self.assertEqual(func, self.function.TRI(0.05, 0.03, 1.3, array))


    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()