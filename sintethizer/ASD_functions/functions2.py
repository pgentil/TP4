import matplotlib.pyplot as plt
import numpy as np
import math

pi = np.pi


def QUARTCOS(self, t0, array):
    values = np.zeros(len(array))
    for t in len(array):
        while array[t] != 1:
            pass
        if array[t] == 1:
            values[t] = np.cos((pi * array[t]) / (2 * t0))
    return values

def HALFCOS(self, t0, array):
    values = np.zeros(len(array))
    index = 0
    for t in len(array):
        if array[t] == 1:
            values[index] = (1 + np.cos(pi * t / t0)) / 2
    return values

def INVLOG(self, t0, duration, frec):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    index = 0
    for t in sample:
        if t < t0:
            values[index] = np.log10((-9 * t) / t0 + 10)
            index += 1
        else:
            values[index] = 0
            index += 1
    return values

def PULSES(self, t0, t1, a1, duration, frec): ##NO FUNCIONA
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    print(values)
    index = 0
    for t in sample:
        tz = (t / t0) - math.floor(t / t0)
        print(tz)
        values[index] = min(abs(((1 - a1) / t1) * (tz - t0 + t1)) + a1)
        print (values)
        index += 1
    return values