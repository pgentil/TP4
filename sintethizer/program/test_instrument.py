import instrument as instrument
from functions import Function

import numpy as np
import matplotlib.pyplot as plt
import unittest

class TestInstruments(unittest.TestCase):

    def setUp(self) -> None:
        self.instrument = instrument.Instrument('ejemplo.txt', 1)
        self.function = Function()
    
    def test_get_functions(self):
        param = ['TRI', 0.05, 0.03, 1.3]
        array = np.array([1,2,3,4,5])
        func = self.instrument.get_functions(param, array)
        self.assertTrue(np.allclose(func, self.function.TRI(0.05, 0.03, 1.3, array)))
        


    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()