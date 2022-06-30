import matplotlib.pyplot as plt
import numpy as np
import math


def TRI(self, t0, t1, a1, array):
    notes = np.zeros(len(array))
    for t in range(len(array)):
        if array[t] < t1:
            notes[t] = array[t] * a1 / t1
        elif t > t1:
            notes[t] = (array[t] - t1) / (t1 - t0)
    return notes

def CONSTANT(self, array):
    return np.ones(len(array))

def INVLINEAR(self, t0, array):
    note = np.zeros(len(array))
    for t in range(len(array)):
        note[t] = max((1 - (array[t] / t0), 0))
    return note

def SIN(self, a, f, array):
    note = np.zeros(len(array))
    for t in range(len(array)):
        note[t] = 1 + (a * np.sin(f * array[t]))
    return note

def INVEXP(self, t0, array):
    note = np.zeros(len(array))
    for t in range(len(array)):
        note[t] = np.exp((-5 * array[t]) / t0)
    return note
