from unittest import registerResult
import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from notespoo import Notes

class Instrument:
    
    def __init__(self, file: str, note: Notes, fs: int):
        self.file = file
        self.harmonics = None
        self.functions = []
        self.note = note
        self.ASD = None
        self.sinoid = None #sintethizer\ASD_functions\instruments\piano.txt
        self.fs = fs
        self.array = None

    def read_instrument(self):
        '''
        Reads the instrument .txt file and saves two different attributes for the Instrument object: harmonics and functions.
        
        ---
        
        filename: str || Must be the name of a .txt file within the 'instruments' folder, containing the number
        of harmonics, the harmonics themselves, and the functions along with their specific parameters.
        
        '''
        waves = {}
        with open(f"sintethizer\ASD_functions\instruments\{self.file}", 'r') as ins:
            harmonic_quantity = int(ins.readline())
            for i in range(harmonic_quantity):
                line = ((ins.readline()).rstrip('\n')).split(' ')
                waves[int(line[0])] = float(line[1])
            self.harmonics = waves
            for line in ins:
                param = line.split(' ')
                for i in range(len(param)):
                    param[i] = param[i].rstrip('\n')
                    if i > 0:
                        param[i] = float(param[i])
                self.functions.append(param)
        self.array = np.linspace(self.note.start, self.note.start + self.note.duration + self.functions[2][1], round(self.fs * (self.note.duration + self.functions[2][1])))
         

    def get_functions(self, param: list, array: np.array) -> np.array:
        '''
        Using a list of parameters (including the name of the function), it executes every function evaluating it with the given array.
        Returns said array evaluated by its designated function.
        
        ---
        
        param: list || A list including the name of the function, followed by its parameters.
        array: np.array || An array representing the X axis with which to evaluate the function. 
        
        '''
        func = Function()
        if param[0] == 'CONSTANT':
            myfunction = func.CONSTANT(array)
        elif param[0] == 'LINEAR':
            myfunction = func.LINEAR(param[1], array)
        elif param[0] == 'INVLINEAR':
            myfunction = func.INVLINEAR(param[1], array)
        elif param[0] == 'EXP':
            myfunction = func.EXP(param[1], array)
        elif param[0] == 'INVEXP':
            myfunction = func.INVEXP(param[1], array)
        elif param[0] == 'QUARTCOS':
            myfunction = func.QUARTCOS(param[1], array)
        elif param[0] == 'QUARTSIN':
            myfunction = func.QUARTSIN(param[1], array)
        elif param[0] == 'HALFCOS':
            myfunction = func.HALFCOS(param[1], array)
        elif param[0] == 'HALFSIN':
            myfunction = func.HALFSIN(param[1], array)
        elif param[0] == 'LOG':
            myfunction = func.LOG(param[1], array)
        elif param[0] == 'INVLOG':
            myfunction = func.INVLOG(param[1], array)
        elif param[0] == 'SIN':
            myfunction = func.SIN(param[1], param[2], array)
        elif param[0] == 'TRI':
            myfunction = func.TRI(param[1], param[2], param[3], array)
        elif param[0] == 'PULSES':
            myfunction = func.PULSES(param[1], param[2], param[3], array)
        else:
            raise AssertionError('The given function is non-existent.')
        return myfunction
    
    def ASD_function(self):
        '''
        Using the "functions" attribute, this function creates the whole "Attack, Sustain, Decay" continuous function.
        The resulting array is assigned to the "ASD" attribute from the Instrument object.
        
        '''
        duration = self.note.duration
        duration_attack = (self.functions[0])[1]
        duration_decay = (self.functions[2])[1]
        asd = self.array[:]
        last_sust_index = len(self.array[self.array <= duration]) - 1
        counter = 0
        for stage in self.functions:
            if counter == 0:
                asd = np.where(self.array > duration_attack, asd, self.get_functions(stage, asd))
            elif counter == 1:
                asd = np.where(np.logical_or((self.array <= duration_attack), (self.array > duration)), asd, self.get_functions(stage, asd))
            elif counter == 2:
                asd = np.where(self.array <= duration, asd, self.get_functions(stage, asd - duration) * (asd[last_sust_index]))
            else:
                raise ValueError('Counter has reached an unintended value.')
            counter += 1
        self.ASD = asd
        plt.plot(self.array, self.ASD)
        plt.show()
        
    def sin(self, intensity, freq):
        start = self.note.start
        result = intensity * np.sin(np.pi * freq * (self.array - start))
        return result
        
    def sinewave(self):
        sinewave = np.zeros(len(self.ASD))

        for i in range(1, len(self.harmonics) + 1):
            newarray = self.sin(self.harmonics[i], self.note.freq * list(self.harmonics.keys())[i - 1])
            sinewave += newarray
        self.sinoid = sinewave

    def full_func(self, amplitude):
        return amplitude * self.ASD * self.sinoid

    def get_full_func(self):
        self.read_instrument()
        self.ASD_function()
        self.sinewave()
        return self.full_func(1)

if __name__ == "__main__":
    nh = [0, 'A4', 0.5]
    note = Notes(nh)
    parameter = 'piano.txt'
    piano = Instrument(parameter, note, 44100)
    array = piano.get_full_func()
    plt.plot(piano.array, array)
    plt.show()