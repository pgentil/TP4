import numpy as np
from functions import Function
import matplotlib.pyplot as plt

def main():
    duration = 5
    duration_attack = 2
    duration_sustain = duration - duration_attack
    duration_decay = 1
    freq = 440
    array_a = np.linspace(0, duration_attack, freq * 15)
    array_s = np.linspace(duration_attack, duration, freq *15)
    array_d = np.linspace(0, duration_decay, freq * 15)
    function = Function()

    attack = function.EXP(duration_attack, array_a)
    print (attack)
    sustain = function.CONSTANT(array_s)
    print(sustain)
    decay = function.INVEXP(duration_decay, array_d)
    print(decay)

    for t in range(len(array_d)):
        array_d[t] += duration



    plt.plot(array_a, attack)
    plt.plot(array_s, sustain)
    plt.plot(array_d, decay)
    plt.show()

if __name__ == "__main__":
    main()