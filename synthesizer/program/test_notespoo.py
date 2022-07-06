from notespoo import Notes
from notes import notes_mapping

import unittest
import numpy as np
class TestNotes(unittest.TestCase):

    def setUp(self) -> None:
        self.note = Notes([0, 'A0', 0.5])
        self.param = [0, 'A0', 0.5]

    def test_soundwave(self):
        array = np.array([1,2,3,4,5,6])
        self.note.soundwave = array
        self.assertTrue(np.allclose(array, self.note.soundwave))

    def test_freq(self):
        for i in notes_mapping:
            if i[0] == self.param[1]:
                freq = i[1]
        self.assertEqual(self.note.freq, i[1])

    def test_duration(self):
        self.assertEqual(self.note.duration, self.param[2])

    def test_start(self):
        self.assertEqual(self.note.start, self.param[0])

    def test_note(self):
        self.assertEqual(self.note.note, self.param[1])
    
    def tearDown(self) -> None:
        del self.note
        del self.param

if __name__ == "__main__":
    unittest.main()