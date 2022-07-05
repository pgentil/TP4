
from instrument import Instrument
from notespoo import Notes
import PRUEBAS


import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import argparse



def main():
    parcer = argparse.ArgumentParser() ##add_argument() ver documentacion
    parcer.add_argument('-f', '--freq', type=str, help='the frequency of the sample rate') #-h para ver que hace cada cosa
    parcer.add_argument('-i', '--instrument', type=str, help='the text file of the instrument\'s configuration')
    parcer.add_argument('-p', '--musicsheet', type=str, help='the text file containing the music sheet')
    parcer.add_argument('')



    parcer = parcer.parse_args() #procesa argumentos que le pases
    print (parcer.name)


    for i in range(parcer.times):
        print(f"hola {parcer.name}")





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
        
    assert np.max(abs(track)) != 0, "The music sheet you've chosen is empty"
    data = 2**15/ np.max(abs(track)) * track

    write("lol.wav", fs, data.astype(np.int16))

    
if __name__ == "__main__":
    main()


#.5 Bb4 .5
# 1 B4 .5
# 1.5 C4 .5
# 2 Db4 .5
# 2.5 D4 .5