from synthesizer.instrument import Instrument
from synthesizer.functions import Function
from synthesizer.notespoo import Notes

import numpy as np
import matplotlib.pyplot as plt
import unittest

class TestInstruments(unittest.TestCase):

    def setUp(self) -> None:
        self.instrument = Instrument('ejemplo.txt', 1)
        self.function = Function()
        self.array = np.array([1,2,3,4,5])
        self.note = Notes([0, 'A0', 6])
    
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
        self.instrument.set_note(self.note)
        sinoid = 0.5 * np.sin(2 * np.pi * self.note.freq * 4)
        result = self.instrument.sin(0.5, self.instrument.note.freq, 4)
        self.assertTrue(np.allclose(sinoid, result))

    def test_sinewave(self):
        self.instrument.set_note(self.note)
        self.instrument.ASD_function()
        self.instrument.sinewave()
        self.assertEqual(self.instrument.sinoid[0], 0)

    def test_full_func(self):
        self.instrument.set_note(self.note)
        self.instrument.ASD_function()
        self.instrument.sinewave()
        self.assertTrue(np.allclose(self.instrument.ASD*self.instrument.sinoid, self.instrument.full_func()))

    def test_get_full_func(self):
        self.instrument.set_note(self.note)
        self.instrument.ASD_function()
        self.instrument.sinewave()
        expected = self.instrument.full_func(0.07)
        result = self.instrument.get_full_func()
        self.assertTrue(np.allclose(expected, result))

    def tearDown(self) -> None:
        del self.instrument
        del self.array
        del self.note
        del self.function


if __name__ == "__main__":
    unittest.main()