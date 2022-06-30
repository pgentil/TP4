import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

pi = np.pi

class Function():
    
    def LINEAR(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note = array[t] / t0
        return note
        
    def EXP(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note[t] = np.exp(5 * (array[t] - t0) / t0)
        return note

    def QUARTSIN(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note[t] = np.sin((pi * array[t]) / (2 * t0))
        return note

    def HALFSIN(self, t0, array):
        note = np.zeros(len(array))
        for t in len(array):
            note[t] = (1 + np.cos(pi * (array[t] / t0 - 0.5))) / 2
        return note

    def LOG(self, t0, array):
        note = np.zeros(len(array))
        for t in len(array):
            note[t] = np.log10(9 * array[t] / t0 + 1)
        return note

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

    def QUARTCOS(self, t0, duration, frec):
        sample = np.arange(0, duration + 1/frec, 1/frec)
        values = np.zeros(len(sample))
        index = 0
        for t in sample:
            values[index] = np.cos((pi * t) / (2 * t0))
            index += 1
        return values

    def HALFCOS(self, t0, duration, frec):
        sample = np.arange(0, duration + 1/frec, 1/frec)
        values = np.zeros(len(sample))
        index = 0
        for t in sample:
            values[index] = (1 + np.cos(pi * t / t0)) / 2
            index += 1
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

        


if __name__ == "__main__":
    function1 = Function()

    result = function1.EXP(2, 0.02, 50)
    print(result)
    x = np.linspace(0, 0.02, 50)
    plt.plot(x, result)
    plt.show()

    def liner(array, t0):
        result = np.zeros(len(array))
        for t in len(array):
            result[t] = array[t] * (1/t0)
        return result
            
    
