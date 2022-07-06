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

def read_scores(score_archive):
    '''
    Reads a song's scores written as a .txt file, line by line. Each line is split into a list of three elements, these being (in order): [start, note, duration].
    Appends each of these lists into a bigger one, called "scores".
    Returns the "scores" list once the program has finished iterating the .txt file lines.
    ---
    score_archive || str. Name of the .txt file containing the song's scores, each line having its own start, note, and duration.
    '''
    with open(f'scores\{score_archive}', 'r') as scr:
        scores = []
        for line in scr:
            line = line.split(' ')
            scores.append(line)
        return scores

def complete_array(big_array, note: Notes, fs: int):
    '''
    Receives the song's array, a note and frequency. Adds a single note's full function into the song's array.
    Returns the song array back again, but with said note's function in it.
    ---
    big_array || np.array. It is the song's full array.
    note || Note object. This object's function will be inserted into the song's array.
    fs || int. This integer, representing the frequency, is used to multiply the song's start.
    '''
    start = int(note.start * fs)
    big_array[start: start + len(note.soundwave)] += note.soundwave
    return big_array

def song_duration(leido):
    '''
    Calculates the duration of the whole song in terms of seconds.
    Returns the calculated duration.
    ---
    leido || list of lists. Each list contains three elements: start, note, duration. Only the start and note elements are used in this function.
    '''
    total_len = 0
    for i in range(len(leido)):
        duration = float(leido[i][0]) + float(leido[i][2])
        if duration > total_len:
            total_len = duration
    return total_len

if __name__ == "__main__":
    pass

    #sample_rate = 44100
