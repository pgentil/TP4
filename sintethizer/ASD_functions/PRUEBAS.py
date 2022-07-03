# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:11:01 2022

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import notes
from scipy.io.wavfile import write

from notespoo import Notes

"""crear un array grande. Leer la nota y crear una funcion,
con su respectiva duración y comienzo(otro array).
Sumar esos arrays chicos al grande. El array grande reemplazarlo
por fun_sen en la creacion del archivo"""

def read_scores(score_archive): #este archivo devuelve lo que dice en escala
    with open(score_archive, 'r') as scr:
        scores = []
        for i in range(12):
            line = (scr.readline()).rstrip('\n')
            line = line.split(' ')
            scores.append(line)
        return scores


def select_freq(read: list, i: int): #la frecuencia de una nota
    for n in range(len(notes.notes_mapping)):
        if notes.notes_mapping[n][0] == read[i][1]:
            return notes.notes_mapping[n][1]


def create_func(freq: float, sample_rate: int, duration_note: float): #la funcio de la dicha nota 
    t = np.arange(0, duration_note, 1/sample_rate)
    print(t)
    freq = freq
    print(freq)
    one_array = 1 * np.sin(2 * np.pi * freq * t)
    return one_array


def complete_array(leido, total_len, score_len, sample_rate): 
    big_array = np.zeros(int(total_len * sample_rate)) #a esto se le debe agregar las muestras del último decay
    for n in range(score_len):
        freq = select_freq(leido, n)
        print(freq)
        func = create_func(freq, sample_rate, float(leido[n][2]))
        start = float(leido[n][0])
        print(start)
        dur = float(leido[n][2])
        print(dur)
        
        big_array[int(start*sample_rate): int((start+dur)*sample_rate)] += func
        
    return big_array


def gen_list_note(scores):
    list_note = []
    for i in scores:
        note = Notes(i)
        list_note.append(note)
    return list_note


leido = read_scores('sintethizer\ASD_functions\escala.txt')
lista = gen_list_note(leido)
lista.sort()
print(lista)

# total_len = float(leido[-1][0]) + float(leido[-1][2])
# print(total_len)
# score_len = len(leido)
# print(score_len)
# song = complete_array(leido, total_len, score_len, 44100)











""" ---------------ESTA PARTE CREA EL ARCHIVO DE AUDIO----------------"""
#armamos una nota 
# duration_note = 4
# sample_rate = 44100
# t = np.arange(0, duration_note, 1/sample_rate)
# freq = 440


# fun_sen = 1 * np.sin(2 * np.pi * freq * t)
#print(fun_sen)

# write('prueba1.wav', sample_rate, song) #fun_sen es la canción entera

""" -----------------------------------------------------------------"""