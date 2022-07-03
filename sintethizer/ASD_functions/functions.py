import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

pi = np.pi

class Function():
    
    def LINEAR(self, t0, array):            
        note = array / t0
        return note
        
    def EXP(self, t0, array):
        note = np.exp(5 * (array - t0) / t0)
        return note

    def QUARTSIN(self, t0, array):
        note = np.sin((pi * array) / (2 * t0))
        return note

    def HALFSIN(self, t0, array):
        note = (1 + np.cos(pi * (array / t0 - 0.5))) / 2
        return note

    def LOG(self, t0, array):
        note = np.log10(9 * array / t0 + 1)
        return note

    def TRI(self, t0, t1, a1, array):
        index = np.where(array == (array[array < t1][-1]))
        print(index)
        notes = np.zeros(len(array))
        notes = np.where(array > t1, notes, array * a1 / t1)
        notes = np.where(array < t1, notes, ((array/(-t0)) + ((t1/t1-t0)) + a1 -(a1-1)))
        # for t in range(len(array)):
        #     if array[t] < t1:
        #         notes[t] = array[t] * a1 / t1
        #     elif t > t1:
        #         notes[t] = (array[t] - t1) / (t1 - t0)
        return notes

    def CONSTANT(self, array):
        return np.ones(len(array))

    def INVLINEAR(self, t0, array):
        note = 1 - (array / t0)
        note[note < 0] = 0
        return note

    def SIN(self, a, f, array):
        note = 1 + (a * np.sin(f * array))
        return note

    def INVEXP(self, t0, array):
        note = np.exp((-5 * array) / t0)
        return note

    def QUARTCOS(self, t0, array):
        note = np.cos((pi * array) / (2 * t0))
        return note

    def HALFCOS(self, t0, array):
        note = (1 + np.cos(pi * array / t0)) / 2
        return note

    def INVLOG(self, t0, array):
        note = np.zeros(len(array))
        note[array <= t0] = np.log10(-9 * array[array <= t0] / t0 + 10)
        note[array > t0] = 0
        return note

    def PULSES(self, t0, t1, a1, array): ##NO FUNCIONA
        prime_t = (array/ t0) - math.floor(array/t0)
        note = np.min(abs(((1-a1)/t0)*(prime_t - t0 + t1)) + a1)
        return note

        


if __name__ == "__main__":
    function1 = Function()

    result = function1.TRI(0.05, 0.03, 1.3, np.linspace(0,0.05, 100))
    print(result)
    x = np.linspace(0,0.05, 100)
    plt.plot(x, result)
    plt.show()

    # def liner(array, t0):
    #     result = array  * (1/t0)
    #     return result
            
    
