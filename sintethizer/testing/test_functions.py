#Testing python file - pytest
import sys
sys.path.append('../')

import unittest
import ASD_functions.asdbis as asdbis
import numpy as np


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.attack = asdbis.Attack()
        self.sustain = asdbis.Sustain()
        self.decay = asdbis.Decay()

    def test_LINEAR(self):
        array = np.array([2, 4, 6, 8])
        self.assertEqual(self.attack.LINEAR(2, 4, 4), array)
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