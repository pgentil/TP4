#/usr/bin/env python
# import sintethizer.program.PRUEBAS as PRUEBAS

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
import argparse

ACCEPTED_NOTES = ['G4, Gs4', 'A4', 'As4', 'Ab4', 'B4', 'Bb4', 'C5', 'Cs5', 'D5', 'Ds5', 'Db5', 'E5', 'Eb5', 'F5', 'G5', 'A5', 'As5', 'Ab5', 'B5', 'Bb5', 'C6', 'Cs6', 'D6', 'Ds6', 'Db6', 'E6', 'Eb6', 'F6', 'Fs6', 'G6', 'Gs6', 'Gb6', 'A6', 'As6', 'Ab6', 'B6', 'Bb6', 'C7', 'Cs7', 'Cb7']

def xylo_read_scores(score_archive):
    '''
    Reads the scores from a song and readapts them for the xylophone to read, swapping the positions of the notes and their starts and outright
    removing the duration. Then, it converts the iterated score into a xylo_object, and appends it into the (once empty) scores list.
    Returns the scores list after all iterations have been processed.
    ---
    score_archive || str. The name of the .txt file containing the song's scores.
    '''
    with open(f'{score_archive}', 'r') as scr:
        scores = []
        for line in scr:
                line = line.split(' ')
                if xylonotes(line) and len(line) != 0:
                        line[1], line[0] = line[0], line[1]
                        line[1] = float(line[1])
                        line.remove(line[2])
                        line = note_velocity(line)
                        # print(line)
                        line = xylo_object(line)
                        scores.append(line)
                else:
                        pass
        return scores

def xylonotes(note:list):
    '''
    Returns all notes within a list that are compatible with the xylophone.
    ---
    notes || list. A list containing N amount of notes, which are strings.
    '''
    return note[1] in ACCEPTED_NOTES

def note_velocity(note: list, velocity=90):
    '''
    Appends the given velocity value into the note list.
    Returns the modified list.
    ---
    note || list. A list containing the notes. It is supposed to be used right after being filtered by the xylonotes method.
    velocity || numeric. The velocity with which the hammers will hit the tile. The default value is 90.
    '''
    note.append(velocity)
    return note

def xylo_object(note: list):
    '''
    
    
    '''
    object = XyloNote(note[0], note[1], note[2])
    return object




def main():
        parcer = argparse.ArgumentParser()
        parcer.add_argument('-i', '--hostip', type=str, help='IP of the host. DEFAULT = \'localhost\'', default='localhost')
        parcer.add_argument('-p', '--port', type=int, help='Port of the server. DEFAULT = 8080', default=8080)
        parcer.add_argument('-s', '--song', type=str, help='The music sheet of the song you want to play.')


        parcer = parcer.parse_args()

        score = parcer.song
        notes = xylo_read_scores(score)

        client = XyloClient(host=parcer.hostip, port=parcer.port)
        client.load(notes)
        client.play()




if __name__ == '__main__':
        main()
        

