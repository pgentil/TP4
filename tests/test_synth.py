import synthesizer.synth as synth
from synthesizer.notespoo import Notes


import unittest
import numpy as np


class TestsynthFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.score = 'escala.txt'
        self.note = Notes([1, 'A4', 2])
        self.array = np.zeros(6)

    def test_read_scores(self):
        notes = synth.read_scores(self.score)
        with open(f'scores/{self.score}', 'r') as scr:
            lines = scr.readlines()
        self.assertEqual(len(notes), len(lines))

    def test_song_duration(self):
        """See 'scores/escala.txt' to see why song_duration = 21."""
        song_duration = 21
        self.assertEqual(song_duration, synth.song_duration(synth.read_scores('escala.txt')))

    def test_complete_array(self):
        decay = 1
        self.note.soundwave = np.arange(0, self.note.duration + decay, 1)
        fs = 1
        expected = np.array([0, 0, 1, 2, 0,0])
        result = synth.complete_array(self.array, self.note, fs)
        print(result)
        self.assertTrue(np.allclose(expected, result))

    
    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()