import numpy as np
import matplotlib.pyplot as plt


from functions import Function
from notespoo import Notes

class Instrument:
    
    def __init__(self, file: str, fs: int):
        """Instrument class that models the behaviuor of an instrument given a certain configuartion and a
        sample rate frequency.
        
        ---

        file || .txt file containing the instrument configurations, including multipliers, harmonics and attack-sustain-decay functions.
        fs ||  the frequency of the samples in each note and its numpy array.

        """
        self.file = file
        self.harmonics = {}
        self.functions = []
        self.note = None
        self.ASD = None
        self.sinoid = None #sintethizer\ASD_functions\instruments\piano.txt
        self.fs = fs
        self.array = None

        with open(f"instruments\{self.file}", 'r') as ins:
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
        """
        Setter method for attribute self.note. Returns none.

        ---

        value || A Notes type object from module notespoo.

        """
        self.note = value
        self._set_array(np.arange(0, value.duration + (self.functions[2])[1], 1/self.fs))


    def _set_array(self, value: np.array):
        """
        Setter method for attribute self.array containing an array that goes from 0 to the duration of the note
        thet will be played. Retruns none.

        ---

        value || A numpy array.

        """
        self.array = value


    def get_functions(self, param: list, array: np.array) -> np.array:
        """
        Using a list of parameters (including the name of the function), it executes every function evaluating it with the given array.
        Returns array evaluated by its designated function.
        
        ---
        
        param: list || A list including the name of the function, followed by its parameters.
        array: np.array || An array representing the X axis with which to evaluate the function. 
        
        """
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
        """
        Using the "functions" attribute, this function creates the whole "Attack, Sustain, Decay" continuous function.
        The resulting array is assigned to the "ASD" attribute from the Instrument object. Returns None.
        
        """
        duration = self.note.duration
        duration_attack = (self.functions[0])[1]
        duration_decay = (self.functions[2])[1]
        asd = self.array[:]
        last_sust_index = len(self.array[self.array <= duration]) - 1
        asd = np.where(self.array < duration_attack, self.get_functions(self.functions[0], asd), np.where(self.array < duration, self.get_functions(self.functions[1], asd), self.get_functions(self.functions[2], asd- duration)))
        self.ASD = asd
        # plt.plot(self.array, self.ASD)
        # plt.show()
        
    def sin(self, intensity: float, freq: float, multiplier: int) -> np.array:
        """
        This method models a sinoid function given the array of the note duration. It returns the result of 
        the whole array modified by the sinoid function. It is the method responsable for the construction of the 
        fundamental and the amronic waves of the note that is being modeled. 
        
        ---

        intensity || The intensity of the wave that modifies the amplitude
        freq || The frequency of the note that is being modeled
        multipliers || The multiplier that will affect the frequency of the wave.

        """
        result = intensity * np.sin(2 * np.pi * freq * multiplier * (self.array)) #intensity * multipliers * 
        return result
        
    def sinewave(self):
        """
        This method carries the task of adding the different armonics of the note in a single array which 
        will result in the final sinoid soundwave of the note. Returns None; instead, it creates a "sinoid" attribute.
        """
        sinewave = np.zeros(len(self.ASD))
        for i in list(self.harmonics.keys()):
            newarray = self.sin(self.harmonics[i], self.note.freq, i)
            sinewave += newarray
        self.sinoid = sinewave 

    def full_func(self, amplitude: float) -> np.array:
        """
        This method carries out the product to generate the final soundwave. It multiplies the final sinoid wave
        with the attack-sustain-decay and an amplitude. It returns a numpy array containing the values that will be modeling the note
        in its final form.
        
        ---

        amplitude || A float that will escalate the final sounwave's amplitude.

        """
        return amplitude * self.ASD * self.sinoid

    def get_full_func(self):
        """
        This method calls all methods needed to create the final soundwave of a note.
        Returns the final soundwave of the note. 

        Warning: The self.note atribute must not be None. It must contain a Notes object from the
        notespoo module.

        """
        self.ASD_function()
        self.sinewave()
        return self.full_func(0.07)

if __name__ == "__main__":
    pass
    # nh = [24, 'A4', 0.1]
    # note = Notes(nh)
    # parameter = 'piano.txt'
    # piano = Instrument(parameter, 441000)
    # piano.set_note(note)
    # array = piano.get_full_func()
    # clean_array = np.arange(0, note.duration+(piano.functions[2])[1], 1/441000)
    
