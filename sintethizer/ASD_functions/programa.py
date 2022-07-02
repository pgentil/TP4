import numpy as np
from functions import Function
import matplotlib.pyplot as plt







def main():
    dictionary = {
        1: 1,
        2: 0.72727272,
        3: 0.31818181,
        4: 0.090909,
    }


    duration = 0.3
    duration_attack = 0.05
    duration_sustain = duration - duration_attack
    duration_decay = 0.02
    freq = 220
    sample = 441000


    function = Function()


    array = np.linspace(0, duration + duration_decay, sample)
    sinoidal = soundwave(array, dictionary ,freq, 0)
    # plt.plot(array, newarray)
    sino = sin(dictionary[2], freq, array, 0)
    newarray = array[array <= duration]
    indexn = np.where(array == newarray[-1])
    print(array[indexn])
    array2 = np.linspace(0, duration + duration_decay, sample)
    array = np.where(array2 > duration_attack, array, function.TRI(duration_attack, 0.03, 1.3, array))
    array = np.where(np.logical_or((array2 <= duration_attack), (array2 > duration)), array, function.CONSTANT(array))
    array = np.where(array2 <= duration, array, function.INVLINEAR(duration_decay, array - duration) * (array[indexn]))


    A = 1
    final = A * array * sinoidal

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

    # plt.plot(array2, sinoidal)
    plt.plot(array2, array)
    plt.plot(array2, final)
    # plt.plot(array_s, sustain)
    # plt.plot(array_d, decay)
    plt.show()


def sin(value, intensity, freq, start):
    result = intensity * np.sin(np.pi * freq * (value - start))
    return result

def soundwave(array: np.array, harmonics: dict, freq, start)-> np.array:
    soundwave = np.zeros(len(array))
    for i in range(1, len(harmonics) + 1):
        newarray = sin(array, harmonics[i], freq * list(harmonics.keys())[i - 1], start)
        soundwave += newarray
    return soundwave


            



if __name__ == "__main__":
    main()