import instrument as instrument
from functions import Function
from notespoo import Notes

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

    def test_set_note(self):
        note = Notes([0, 'A4', 0.5])
        self.instrument.set_note(note)
        self.assertTrue(self.instrument.note.freq == note.freq and self.instrument.note.duration == note.duration and self.instrument.note.start == note.start and len(self.instrument.array) != 0 )

    def

        


    def tearDown(self) -> None:
        del self.instrument
        del self.function


if __name__ == "__main__":
    unittest.main()