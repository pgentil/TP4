
from instrument import Instrument
from notespoo import Notes
import synth


import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import argparse



def main():
    parcer = argparse.ArgumentParser() ##add_argument() ver documentacion
    parcer.add_argument('-f', '--freq', choices=[8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000] ,type=int, help='the frequency of the sample rate') #-h para ver que hace cada cosa
    parcer.add_argument('-i', '--input', type=str, help='the text file of the instrument\'s configuration')
    parcer.add_argument('-p', '--musicsheet', type=str, help='the text file containing the music sheet')
    parcer.add_argument('-o', '--output', type=str, help='the title of the wave file that is going to be written')



    parcer = parcer.parse_args() #procesa argumentos que le pases
    print(parcer.freq, parcer.input, parcer.musicsheet, parcer.output)

    
    assert (parcer.input != None), 'No instrument was inputed'
    assert (parcer.musicsheet != None), 'No music sheet was selected'
    if parcer.output == None:
        parcer.output = 'song.wav'
    scores = parcer.musicsheet
    instrument = parcer.input
    if parcer.freq == None: 
        fs = 48000
    else:
        fs = parcer.freq

    piano = Instrument(instrument, fs) 
    decay_duration = piano.functions[2][1]

    SCORES = synth.read_scores(scores) #lista de lista con c renglon de la partitura
    song_duration = synth.song_duration(SCORES)  #devuelve la dur de la cancion en segundos
    print(fs)
    track = np.zeros(round((song_duration + decay_duration)*fs) + fs) #array de ceros a completar

    for i in SCORES:
        # print(i)
        note = Notes(i)#el renglon num i de la partitura
        # print(note.start, note.note, note.duration)
        piano.set_note(note)
        # print(f'nota: {note}')  #F4
        note.soundwave = piano.get_full_func() #devuelve la senial de la nota con asd y armonicos incluidos
        track = synth.complete_array(track ,note, fs)
        
    assert np.max(abs(track)) != 0, "The music sheet you've chosen is empty"
    data = 2**15/ np.max(abs(track)) * track

    write(parcer.output, fs, data.astype(np.int16))

    
if __name__ == "__main__":
    main()


#.5 Bb4 .5
# 1 B4 .5
# 1.5 C4 .5
# 2 Db4 .5
# 2.5 D4 .5