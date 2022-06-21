import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

class Function():
    
    def __init__(self):
        self.attack = None
        self.sustain = None
        self.decay = None
        
    def __str__(self):
        return f"ATTACK: {self.attack}\nSUSTAIN: {self.sustain}\nDECAY: {self.decay}"
        
    def LINEAR(self, t0, duration, frec):
        sample = np.arange(0, duration + 1/frec, 1/frec)
        values = np.zeros(len(sample))
        print(sample)
        index = 0
        for t in sample:
            print (t)
            print(values[index])
            values[index] = t / t0
            index += 1
            print(index)
            print(t/t0)
        return values
        
    def EXP(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.exp(5 * (t - t0) / t0)
        return values

    def QUARTSIN(self, t0, duration, frec):
        values = np.zeros(0, duration, frec)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.sin((pi * t) / (2 * t0))
        return values

    def HALFSIN(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (1 + np.cos(pi * (t / t0 - 0.5))) / 2
        return values

    def LOG(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.log10(9 * t / t0 + 1)
        return values

    def TRI(self, t0, t1, a1, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            if t < t1:
                values[t] = t * a1 / t1
            elif t > t1:
                values[t] = (t - t1) / (t1 - t0)
        return values

    def CONSTANT(self, duration, frec):
        return np.ones(duration)

    def INVLINEAR(self, t0, duration, frec: str):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (max(1 - (t / t0)))

    def SIN(self, a, f, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = 1 + (a * np.sin(f * t))

    def INVEXP(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.exp((-5 * t) / t0)
        return values

    def QUARTCOS(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = np.cos((pi * t) / (2 * t0))
        return values

    def HALFCOS(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            values[t] = (1 + np.cos(pi * t / t0)) / 2
        return values

    def INVLOG(self, t0, duration, frec):
        
        values = np.zeros(duration)
        for t in np.arange(0, duration, 1/frec):
            if t < t0:
                values[t] = np.log10((-9 * t) / t0 + 10)
            else:
                values[t] = 0
        return values

    def PULSES(self, t0, t1, a1, duration, frec):
        return NotImplementedError


if __name__ == "__main__":
    function1 = Function()
    print(function1.LINEAR(0.5, 60, 4))