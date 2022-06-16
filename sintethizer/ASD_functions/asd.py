import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

  
def LINEAR(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = t / t0
    return values
    
def EXP(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = np.exp(5 * (t - t0) / t0)
    return values

def QUARTSIN(t0, duration, frec):
    values = np.zeros(0, duration, frec)
    for t in np.linspace(0, duration, frec):
        values[t] = np.sin((pi * t) / (2 * t0))
    return values

def HALFSIN(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = (1 + np.cos(pi * (t / t0 - 0.5))) / 2
    return values

def LOG(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = np.log10(9 * t / t0 + 1)
    return values

def TRI(t0, t1, a1, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        if t < t1:
            values[t] = t * a1 / t1
        elif t > t1:
            values[t] = (t - t1) / (t1 - t0)
    return values

def CONSTANT(duration, frec):
    return np.ones(duration)

def INVLINEAR(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = (max(1 - (t / t0)))
    return values

def SIN(a, f, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = 1 + (a * np.sin(f * t))
    return values

def INVEXP(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = np.exp((-5 * t) / t0)
    return values

def QUARTCOS(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = np.cos((pi * t) / (2 * t0))
    return values

def HALFCOS(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        values[t] = (1 + np.cos(pi * t / t0)) / 2
    return values

def INVLOG(t0, duration, frec):
    values = np.zeros(duration)
    for t in np.linspace(0, duration, frec):
        if t < t0:
            values[t] = np.log10((-9 * t) / t0 + 10)
        else:
            values[t] = 0
    return values

def PULSES(t0, t1, a1, duration, frec):
    return NotImplementedError