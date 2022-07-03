import numpy as np
import matplotlib.pyplot as plt
from functions import Function

class Instrument:
    def __init__(self, instrument):
        self.instrument = instrument
        self.harmonics = None
        self.functions = []

    def read_instrument(self, filename):
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
    

# def read_instrument1(instrument) -> list:
#     data = []
#     with open(f"instruments/{instrument}", 'r') as ins:
#         for line in ins:
#             line.rstrip('\n')
#             info = line.split()
#             for i in range(len(info)):
#                 if '.' in info[i]:
#                     info[i] = float(info[i])
#                 elif info[i].isnumeric() == True:
#                     info[i] = int(info[i])
#             data.append(info)
#     return data

# La función de acá arriba ya quedó obsoleta, pero la comento por las dudas

if __name__ == "__main__":
    piano = Instrument('Piano')
    piano.read_instrument('piano.txt')
    print(piano.harmonics)
    print(piano.functions)