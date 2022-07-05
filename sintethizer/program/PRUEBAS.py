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
    with open(f'sintethizer\program\scores\{score_archive}', 'r') as scr:
        scores = []
        for line in scr:
            line = line.split(' ')
            scores.append(line)
        return scores


def select_freq(read: list, i: int): #la frecuencia de una nota
    for n in range(len(notes.notes_mapping)):
        if notes.notes_mapping[n][0] == read[i][1]:
            return notes.notes_mapping[n][1]


def create_func(freq: float, sample_rate: int, duration_note: float): #la funcio de la dicha nota 
    t = np.arange(0, duration_note, 1/sample_rate)
    one_array = 1 * np.sin(2 * np.pi * freq * t)
    return one_array


# def complete_array(leido, total_len, score_len, sample_rate): 
#     big_array = np.zeros(int(total_len * sample_rate)+1) #a esto se le debe agregar las muestras del último decay
#     print(f'Big array: {len(big_array)}')
#     for n in range(score_len):
#         freq = select_freq(leido, n)
#         #print(freq)
#         func = create_func(freq, sample_rate, float(leido[n][2]))
#         start = int(float(leido[n][0]) * sample_rate)
#         #print(start)
#         end = len(func) + start 
#         #print(end)
        
#         big_array[start:end] += func
        
#     return big_array

def complete_array(big_array, note: Notes, fs: int, decay_duration): 
    # print(f'Big array: {len(big_array)}')
    # print(note.start)
    # print(note.duration)
    # print(note.soundwave)

    # print(len(big_array[round(note.start * fs): round((note.start) * fs) + len(note.soundwave)]))
    # print(len(note.soundwave))
    start = int(note.start * fs)
    big_array[start: start + len(note.soundwave)] += note.soundwave
    # print(big_array) 
    # for i in range(start, start+20):
    #     print(big_array[i])
    return big_array




def song_duration(leido):
    total_len = 0
    for i in range(len(leido)):
        duration = float(leido[i][0]) + float(leido[i][2])
        if duration > total_len:
            total_len = duration
    return total_len



def create_song(archive_name, sample_rate, array_song):
    """
    Creates a wavefile
    Parameters
    ----------
    archive_name : String
        The archive's name.
    sample_rate : Int
        Generally 44100.
    array_song : Array
        Array which contains the functions values.

    """
    write(archive_name, sample_rate, array_song)

if __name__ == "__main__":


    leido = read_scores('debussy-clair-de-lune.txt')
    # print(leido)
    score_len = len(leido)
    #print(score_len)
    total_len = song_duration(leido)
    # print(total_len)
    song = complete_array(leido, total_len, score_len, 44100)



    sample_rate = 44100
