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


    array = np.linspace(0, duration + duration_decay, sample) ## FUNCION CAMELLO SIN MODIFICAR
    sinoidal = soundwave(array, dictionary ,freq, 0) ## FUNCION SINODIAL HAY QUE CAMBIARLE EL NOMBRE A INGLES
    # plt.plot(array, newarray)
    sino = sin(dictionary[2], freq, array, 0) ##FUNCION DE PRUEBA DE SOLO UNA FUNCION SENO SIN INCLUIR A LA SUMA DE SINOIDALES
    newarray = array[array <= duration] ## ARRAY PARA AGARRAR EL ULTIMO ELEMENTO ANTES DEL DECAY
    array2 = np.linspace(0, duration + duration_decay, sample) ## EJE X PARA EL PLOT
    array = np.where(array2 > duration_attack, array, function.TRI(duration_attack, 0.03, 1.3, array))
    array = np.where(np.logical_or((array2 <= duration_attack), (array2 > duration)), array, function.CONSTANT(array))
    array = np.where(array2 <= duration, array, function.INVLINEAR(duration_decay, array - duration) * (array[len(newarray)-1]))


    A = 1 ##AMPLITUD
    final = A * array * sinoidal ## EN EL ENUNCIADO ESTA COMO A*y(t)*m(t)

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
    # plt.plot(array_s, sustain)
    # plt.plot(array_d, decay)

    plt.plot(array2, array)
    plt.plot(array2, final)
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