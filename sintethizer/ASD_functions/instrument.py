import numpy as np
import matplotlib.pyplot as plt
from functions import Function

class Instrument:
    
    def __init__(self, instrument: str, note: Note):
        self.instrument = instrument
        self.harmonics = None
        self.functions = []
        self.note = note

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
                
    def get_functions(self, param: list, array: np.array):
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
        duration = self.note.duration
        freq = self.note.freq
        duration_attack = (self.functions[0])[1]
        duration_sustain = duration - duration_attack
        duration_decay = (self.functions[2])[1]
        

#%% 


if __name__ == "__main__":
    piano = Instrument('Piano', 4)
    piano.read_instrument('piano.txt')
    
    # duration = 0.3
    # duration_attack = 0.05
    # duration_sustain = duration - duration_attack
    # duration_decay = 0.02
    # freq = 220
    # sample = 441000
    
    # array = np.linspace(0, duration + duration_decay, sample)
    # last_sustained_index = len(array[array <= duration])-1
    # array = np.where(array2 > duration_attack, array, function.TRI(duration_attack, 0.03, 1.3, array))
    # array = np.where(np.logical_or((array2 <= duration_attack), (array2 > duration)), array, function.CONSTANT(array))
    # array = np.where(array2 <= duration, array, function.INVLINEAR(duration_decay, array - duration) * (array[last_sustained_index]))