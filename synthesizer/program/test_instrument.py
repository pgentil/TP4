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
        self.array = np.array([1,2,3,4,5])
        self.note = Notes([0, 'A0', 0.5])
    
    def test_get_functions(self):
        param = ['TRI', 0.05, 0.03, 1.3]
        self.array
        func = self.instrument.get_functions(param, self.array)
        self.assertTrue(np.allclose(func, self.function.TRI(0.05, 0.03, 1.3, self.array)))

    def test_set_note(self):
        self.instrument.set_note(self.note)
        self.assertTrue(self.instrument.note.freq == self.note.freq and self.instrument.note.duration == self.note.duration and self.instrument.note.start == self.note.start and len(self.instrument.array) != 0 )

    def test_ASD_function(self):
        self.instrument.set_note(self.note)
        expected = self.instrument.array[:]
        expected = np.where(self.instrument.array < self.instrument.functions[0][1], self.instrument.get_functions(self.instrument.functions[0], expected), np.where(self.instrument.array < self.note.duration, self.instrument.get_functions(self.instrument.functions[1], expected), self.instrument.get_functions(self.instrument.functions[2], expected- self.note.duration)))
        self.instrument.ASD_function()
        self.assertTrue(np.allclose(expected, self.instrument.ASD))
        pass

    def test_sin(self):
        pass

    def test_sinewave(self):
        pass

    def test_full_func(self):
        pass

    def test_get_full_func(self):
        pass

    def tearDown(self) -> None:
        del self.instrument
        del self.array
        del self.note
        del self.function


if __name__ == "__main__":
    unittest.main()