from tracemalloc import start
import numpy as np
from regex import F
from functions import Function
import matplotlib.pyplot as plt







def main():
    dictionary = {
        1: 1,
        2: 0.72727272,
        3: 0.31818181,
        4: 0.090909
    }
    duration = 5
    duration_attack = 2
    duration_sustain = duration - duration_attack
    duration_decay = 1
    freq = 440
    function = Function()
    array = np.linspace(0, duration + duration_decay, freq)
    sinoidal = soundwave(array, dictionary ,freq, 0)
    # plt.plot(array, newarray)

    newarray = array[array <= duration]
    indexn = np.where(array == newarray[-1])
    array2 = np.linspace(0, duration + duration_decay, freq)
    array = np.where(array > duration_attack, array, function.EXP(duration_attack, array))
    array = np.where(np.logical_or((array <= duration_attack), (array > duration)), array, function.CONSTANT(array))
    array = np.where(array <= duration, array, function.INVEXP(duration_decay, array - duration) * (array[indexn] - 0.2))

    final = array * sinoidal

    # array_a = np.linspace(0, duration_attack, freq * 15)
    # array_s = np.linspace(duration_attack, duration, freq *15)
    # array_d = np.linspace(0, duration_decay, freq * 15)

    # attack = function.EXP(duration_attack, array_a)
    # print (attack)
    # sustain = function.CONSTANT(array_s)
    # print(sustain)
    # decay = function.INVEXP(duration_decay, array_d)
    # print(decay)

    # for t in range(len(array_d)):
    #     array_d[t] += duration

    
    plt.plot(array2, final)
    # plt.plot(array_s, sustain)
    # plt.plot(array_d, decay)
    plt.show()


def sin(intensity, freq, value, start):
    result = intensity * np.sin(np.pi * freq * (value - start))
    return result

def soundwave(array: np.array, harmonics: dict, freq, start)-> np.array:
    soundwave = np.zeros(len(array))
    for i in range(1, len(harmonics) + 1):
        newarray = sin(harmonics[i], freq * list(harmonics.keys())[i - 1], array, start)
        soundwave += newarray
    return soundwave


            



if __name__ == "__main__":
    main()