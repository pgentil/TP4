import numpy as np
from functions import Function
import matplotlib.pyplot as plt

def main():
    duration = 5
    duration_attack = 2
    duration_sustain = duration - duration_attack
    duration_decay = 1
    freq = 440
    array = np.linspace(0, duration + duration_decay, freq *15)
    array_a = np.linspace(0, duration_attack, freq * 15)
    array_s = np.linspace(duration_attack, duration, freq *15)
    array_d = np.linspace(duration, duration + duration_decay, freq*15)
    function = Function()

    attack = function.EXP(duration_attack, array_a)
    sustain = function.CONSTANT(duration_sustain, array_s)
    decay = function.INVLINEAR(duration_decay, array_d)
    
    plt.plot(array, attack)
    plt.plot(array, sustain)
    plt.plot(array, decay)
    plt.show()

if __name__ == "__main__":
    main()