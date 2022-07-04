from functions import Function
from instrument import Instrument
from notespoo import Notes
import PRUEBAS
import numpy as np
import synthesizer

scores = 'queen.txt'
instrument = 'piano.txt'
fs = 44100

piano = Instrument(instrument, fs) 
decay_duration = piano.functions[2][1]

SCORES = PRUEBAS.read_scores(scores) #lista de lista con c renglon de la partitura
song_duration = round(PRUEBAS.song_duration(SCORES))  #devuelve la dur de la cancion en segundos
big_array = np.zeros(round(song_duration * fs) + round(decay_duration * fs) + 1) #array de ceros a completar

for i in SCORES:
    note = Notes(i)  #el renglon num i de la partitura
    piano.set_note(note)
    print(f'nota: {note}')  #F4
    note.soundwave = piano.get_full_func() #devuelve la senial de la nota con asd y armonicos incluidos

    big_array = PRUEBAS.complete_array(big_array ,note, fs, decay_duration)

synthesizer.create_song("lol.wav", fs, big_array)

    



