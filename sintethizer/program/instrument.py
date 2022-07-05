from unittest import registerResult
import numpy as np
import matplotlib.pyplot as plt
from functions import Function
from notespoo import Notes

class Instrument:
    
    def __init__(self, file: str, fs: int):
        self.file = file
        self.harmonics = {}
        self.functions = []
        self.note = None
        self.ASD = None
        self.sinoid = None #sintethizer\ASD_functions\instruments\piano.txt
        self.fs = fs
        self.array = None

        with open(f"sintethizer\ASD_functions\instruments\{self.file}", 'r') as ins:
            harmonic_quantity = int(ins.readline())
            for i in range(harmonic_quantity):
                line = ((ins.readline()).rstrip('\n')).split(' ')
                self.harmonics[int(line[0])] = float(line[1])
            for line in ins:
                param = line.split(' ')
                for i in range(len(param)):
                    param[i] = param[i].rstrip('\n')
                    if i > 0:
                        param[i] = float(param[i])
                self.functions.append(param)
      
    



    def set_note(self, value: Notes):
        self.note = value
        self.set_array(np.arange(0, value.duration + (self.functions[2])[1], 1/self.fs))

    


    def set_array(self, value: np.array):
        self.array = value

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
        
    def sin(self, intensity, freq, multipliers):
        result = intensity * np.sin(2 * np.pi * freq * multipliers * (self.array)) #intensity * multipliers * 
        return result
        
    def sinewave(self):
        sinewave = np.zeros(len(self.ASD))
        for i in list(self.harmonics.keys()):
            newarray = self.sin(self.harmonics[i], self.note.freq, i)
            sinewave += newarray
        self.sinoid = sinewave 

    def full_func(self, amplitude):
        return amplitude * self.ASD * self.sinoid

    def get_full_func(self):
        self.ASD_function()
        self.sinewave()
        return self.full_func(0.005)

if __name__ == "__main__":
    nh = [24, 'A4', 0.1]
    note = Notes(nh)
    parameter = 'piano.txt'
    piano = Instrument(parameter, 441000)
    piano.set_note(note)
    array = piano.get_full_func()
    clean_array = np.arange(0, note.duration+(piano.functions[2])[1], 1/441000)
    plt.plot(clean_array, array)
    plt.show()