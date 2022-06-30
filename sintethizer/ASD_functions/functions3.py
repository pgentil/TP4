import matplotlib.pyplot as plt
import numpy as np
import math


def TRI(self, t0, t1, a1, duration, frec):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    index = 0
    for t in sample:
        if t < t1:
            values[index] = t * a1 / t1
            index += 1
        elif t > t1:
            values[index] = (t - t1) / (t1 - t0)
            index += 1
    return values

def CONSTANT(self, duration, frec):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    return np.ones(len(sample))

def INVLINEAR(self, t0, duration, frec: str):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    index = 0
    for t in sample:
        values[index] = (max(1 - (t / t0)))
        index += 1
    return values

def SIN(self, a, f, duration, frec):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    index = 0
    for t in sample:
        values[index] = 1 + (a * np.sin(f * t))
        index += 1
    return values

def INVEXP(self, t0, duration, frec):
    sample = np.arange(0, duration + 1/frec, 1/frec)
    values = np.zeros(len(sample))
    index = 0
    for t in sample:
        values[index] = np.exp((-5 * t) / t0)
        index += 1
    return values