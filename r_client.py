#/usr/bin/env python
# import sintethizer.program.PRUEBAS as PRUEBAS

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
import argparse



def xylo_read_scores(score_archive): #este archivo devuelve lo que dice en escala
    with open(f'{score_archive}', 'r') as scr:
        scores = []
        for line in scr:
                print(line)
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
    accepted_notes = ['G4, Gs4', 'A4', 'As4', 'Ab4', 'B4', 'Bb4', 'C5', 'Cs5', 'D5', 'Ds5', 'Db5', 'E5', 'Eb5', 'F5', 'G5', 'A5', 'As5', 'Ab5', 'B5', 'Bb5', 'C6', 'Cs6', 'D6', 'Ds6', 'Db6', 'E6', 'Eb6', 'F6', 'Fs6', 'G6', 'Gs6', 'Gb6', 'A6', 'As6', 'Ab6', 'B6', 'Bb6', 'C7', 'Cs7', 'Cb7']
    return note[1] in accepted_notes

def note_velocity(note: list, velocity=90):
        note.append(velocity)
        return note

def xylo_object(note: list):
        print(type(note[1]))
        object = XyloNote(note[0], note[1], note[2])
        return object




def main():
        # parcer = argparse.ArgumentParser()
        # parcer.add_argument('-h', '--host', type=str, help='IP of the host')

        # parcer = parcer.parse_args()
        # print(parcer.host)

        score = 'sintethizer/program/scores/wii.txt'
        notes = xylo_read_scores(score)
        print(notes)

        client = XyloClient(host='localhost', port=8080)
        client.load(notes)
        client.play()




if __name__ == '__main__':
        main()
        

