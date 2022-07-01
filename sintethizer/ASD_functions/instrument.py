import numpy as np
import matplotlib.pyplot as plt
from functions import Function

class Instrument:
    def __init__(self, instrument):
        self.instrument = instrument
        self.harmonics = None

    def read_instrument(self, instrument):
        waves = {}
        with open(f"/{instrument}", 'r') as ins: #instruments/
            harmonics = int(ins.readline())
            for i in range(harmonics):
                line = (ins.readline()).rstrip('\n')
                line = line.split(' ')
                waves[int(line[0])] = float(line[1])
            self.harmonics = waves




def get_func(param: list, array):
        func = Function()
        if param[0] == 'CONSTANT':
            func.CONSTANT(array)
        elif param[0] == 'LINEAR':
            func.LINEAR(param[1], array)
        elif param[0] == 'INVLINEAR':
            func.INVLINEAR(param[1], array)
        elif param[0] == 'EXP':
            func.EXP(param[1], array)
        elif param[0] == 'INVEXP':
            func.INVEXP(param[1], array)
        elif param[0] == 'QUARTCOS':
            func.QUARTCOS(param[1], array)
        elif param[0] == 'QUARTSIN':
            func.QUARTSIN(param[1], array)
        elif param[0] == 'HALFCOS':
            func.HALFCOS(param[1], array)
        elif param[0] == 'HALFSIN':
            func.HALFSIN(param[1], array)
        elif param[0] == 'LOG':
            func.LOG(param[1], array)
        elif param[0] == 'INVLOG':
            func.INVLOG(param[1], array)
        elif param[0] == 'SIN':
            func.SIN(param[1], param[2], array)
        elif param[0] == 'TRI':
            func.TRI(param[1], param[2], param[3], array)
        elif param[0] == 'PULSES':
            func.PULSES(param[1], param[2], param[3], array)
        else:
            raise AssertionError('The given function is non-existant.')
        return func
    

def read_instrument1(instrument) -> list:
    data = []
    with open(f"/{instrument}", 'r') as ins:
        for line in ins:
            line.rstrip('\n')
            info = line.split()
            for i in range(len(info)):
                if '.' in info[i]:
                    info[i] = float(info[i])
                elif info[i].isnumeric() == True:
                    info[i] = int(info[i])
            data.append(info)
    return data

if __name__ == "__main__":
    piano = Instrument("piano.txt")
    # piano.read_instrument('piano.txt')
    # print(piano.harmonics)

    print(read_instrument1("piano.txt"))