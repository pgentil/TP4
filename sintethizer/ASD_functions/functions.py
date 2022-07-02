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
        #note = np.zeros(len(array))
        #for t in range(len(array)):
           # note[t] = np.exp(5 * (array[t] - t0) / t0)
        
        note = np.exp(5 * (array - t0) / t0)
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
        #for t in range(len(array)):
         #   note[t] = max((1 - (array[t] / t0), 0))
        
        note = 1 - (array / t0)
        note[array < 0] = 0
        return note

    def SIN(self, a, f, array):
        note = np.zeros(len(array))
        #for t in range(len(array)):
            #note[t] = 1 + (a * np.sin(f * array[t]))
        
        note = 1 + (a * np.sin(f * array))
        return note

    def INVEXP(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note[t] = np.exp((-5 * array[t]) / t0)
        return note

    def QUARTCOS(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note[t] = np.cos((pi * array[t]) / (2 * t0))
        return note

    def HALFCOS(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            note[t] = (1 + np.cos(pi * t / t0)) / 2
        return note

    def INVLOG(self, t0, array):
        note = np.zeros(len(array))
        for t in range(len(array)):
            if t < t0:
                note[t] = np.log10((-9 * t) / t0 + 10)
            else:
                note[t] = 0
        return note

    def PULSES(self, t0, t1, a1, array): ##NO FUNCIONA
        note = np.zeros(len(array))
        print(note)
        for t in range(len(array)):
            tz = (array[t] / t0) - math.floor(array[t] / t0)
            print(tz)
            note[t] = min(abs(((1 - a1) / t1) * (tz - t0 + t1)) + a1)
            print (note)
        return note

        


if __name__ == "__main__":
    function1 = Function()

    result = function1.INVLINEAR(3, np.array([1, 2, 3, 4, 5, 6]))
    print(result)
    x = np.linspace(0, 1, 6)
    plt.plot(x, result)
    plt.show()

    def liner(array, t0):
        result = np.zeros(len(array))
        for t in len(array):
            result[t] = array[t] * (1/t0)
        return result
            
    
