from functions import Function
from instrument import Instrument
from notespoo import Notes
import PRUEBAS
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

scores = 'uptown_funk.txt'
instrument = 'piano.txt'
fs = 44100

piano = Instrument(instrument, fs) 
decay_duration = piano.functions[2][1]

SCORES = PRUEBAS.read_scores(scores) #lista de lista con c renglon de la partitura
song_duration = PRUEBAS.song_duration(SCORES)  #devuelve la dur de la cancion en segundos
track = np.zeros(round((song_duration + decay_duration)*fs) + 1 * fs) #array de ceros a completar

for i in SCORES:
    # print(i)
    note = Notes(i)#el renglon num i de la partitura
    # print(note.start, note.note, note.duration)
    piano.set_note(note)
    # print(f'nota: {note}')  #F4
    note.soundwave = piano.get_full_func() #devuelve la senial de la nota con asd y armonicos incluidos
    track = PRUEBAS.complete_array(track ,note, fs, decay_duration)
    

data = 2**15/ np.max(abs(track)) * track
write("lol.wav", fs, data.astype(np.int16))

    



#.5 Bb4 .5
# 1 B4 .5
# 1.5 C4 .5
# 2 Db4 .5
# 2.5 D4 .5