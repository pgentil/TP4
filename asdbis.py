import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

class Function():
    
    def __init__(self):
        self.attack = None
        self.sustain = None
        self.decay = None
        
    def LINEAR(self, t0, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = t / t0
        self.attack = values
        
    def EXP(self, t0, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.exp(5 * (t - t0) / t0)
        self.attack = values

    def QUARTSIN(self, t0, duration, frec):
        values = np.zeros(0, duration, frec)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.sin((pi * t) / (2 * t0))
        self.attack = values

    def HALFSIN(self, t0, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (1 + np.cos(pi * (t / t0 - 0.5))) / 2
        self.attack = values

    def LOG(self, t0, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.log10(9 * t / t0 + 1)
        self.attack = values

    def TRI(self, t0, t1, a1, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            if t < t1:
                values[t] = t * a1 / t1
            elif t > t1:
                values[t] = (t - t1) / (t1 - t0)
        self.attack = values

    def CONSTANT(self, duration, frec):
        self.sustain = np.ones(duration)

    def INVLINEAR(self, t0, duration, frec, use: str):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (max(1 - (t / t0)))
        if use == 'S':
            self.sustain = values
        elif use == 'D':
            self.decay = values

    def SIN(self, a, f, duration, frec):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = 1 + (a * np.sin(f * t))
        self.sustain = values

    def INVEXP(self, t0, duration, frec, use):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.exp((-5 * t) / t0)
        if use == 'S':
            self.sustain = values
        elif use == 'D':
            self.decay = values

    def QUARTCOS(self, t0, duration, frec, use):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.cos((pi * t) / (2 * t0))
        if use == 'S':
            self.sustain = values
        elif use == 'D':
            self.decay = values

    def HALFCOS(self, t0, duration, frec, use):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (1 + np.cos(pi * t / t0)) / 2
        if use == 'S':
            self.sustain = values
        elif use == 'D':
            self.decay = values

    def INVLOG(self, t0, duration, frec, use):
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            if t < t0:
                values[t] = np.log10((-9 * t) / t0 + 10)
            else:
                values[t] = 0
        if use == 'S':
            self.sustain = values
        elif use == 'D':
            self.decay = values

    def PULSES(self, t0, t1, a1, duration, frec):
        return NotImplementedError