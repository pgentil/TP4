import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from notespoo import Notes

class Instrument:
    
    def __init__(self, instrument: str, note: Notes):
        self.instrument = instrument
        self.harmonics = None
        self.functions = []
        self.note = note
        self.ASD = None
        self.sin = None #sintethizer\ASD_functions\instruments\piano.txt

    def read_instrument(self, filename: str):
        '''
        Reads the instrument .txt file and saves two different attributes for the Instrument object: harmonics and functions.
        
        ---
        
        filename: str || Must be the name of a .txt file within the 'instruments' folder, containing the number
        of harmonics, the harmonics themselves, and the functions along with their specific parameters.
        
        '''
        waves = {}
        with open(f"instruments/{filename}", 'r') as ins:
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
    
    def ASD_function(self, iterations: int):
        '''
        Using the "functions" attribute, this function creates the whole "Attack, Sustain, Decay" continuous function.
        The resulting array is assigned to the "ASD" attribute from the Instrument object.
        
        '''
        duration = self.note.duration
        duration_attack = (self.functions[0])[1]
        duration_decay = (self.functions[2])[1]
        array, clean_array = np.linspace(0, duration + duration_decay, iterations), np.linspace(0, duration + duration_decay, iterations)
        last_sust_index = len(array[array <= duration]) - 1
        counter = 0
        for stage in self.functions:
            if counter == 0:
                array = np.where(clean_array > duration_attack, array, self.get_functions(stage, array))
            elif counter == 1:
                array = np.where(np.logical_or((clean_array <= duration_attack), (clean_array > duration)), array, self.get_functions(stage, array))
            elif counter == 2:
                array = np.where(clean_array <= duration, array, self.get_functions(stage, array - duration) * (array[last_sust_index]))
            else:
                raise ValueError('Counter has reached an unintended value.')
            counter += 1
        self.ASD = array
        
    def sin(self, array, intensity):
        start, freq = self.note.start, self.note.freq
        result = intensity * np.sin(np.pi * freq * (array - start))
        return result
        
    def sinewave(self):
        sinewave = np.zeros(len(self.ASD))
        for i in range(1, len(self.harmonics) + 1):
            newarray = self.sin(self.ASD, self.harmonics[i], self.note.freq * list(self.harmonics.keys())[i - 1], self.note.start)
            sinewave += newarray
        self.sin = sinewave

    def get_full_func(self, amplitude):
        return amplitude * self.ASD * self.sin

if __name__ == "__main__":
    nh = [0, 'C8', 0.5]
    note = Notes(nh)
    piano = Instrument('Piano', note)
    piano.read_instrument('piano.txt')
    piano.ASD_function(44100)
    