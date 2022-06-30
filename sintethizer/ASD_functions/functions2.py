import matplotlib.pyplot as plt
import numpy as np
import math

from pyrsistent import T

pi = np.pi


def QUARTCOS(self, t0, array):
    note = np.zeros(len(array))
    for t in len(array):
        note[t] = np.cos((pi * array[t]) / (2 * t0))
    return note

def HALFCOS(self, t0, array):
    note = np.zeros(len(array))
    for t in len(array):
        note[t] = (1 + np.cos(pi * t / t0)) / 2
    return note

def INVLOG(self, t0, array):
    note = np.zeros(len(array))
    for t in len(array):
        if t < t0:
            note[t] = np.log10((-9 * t) / t0 + 10)
        else:
            note[t] = 0
    return note

def PULSES(self, t0, t1, a1, array): ##NO FUNCIONA
    note = np.zeros(len(array))
    print(note)
    for t in len(array):
        tz = (array[t] / t0) - math.floor(array[t] / t0)
        print(tz)
        note[t] = min(abs(((1 - a1) / t1) * (tz - t0 + t1)) + a1)
        print (note)
    return note