import numpy as np
import matplotlib.pyplot as plt
from asdbis import Function


def get_func(param: list, duration, fs, use):
        func = Function()
        if param[0] == 'CONSTANT':
            func.CONSTANT(duration, fs, use)
        elif param[0] == 'LINEAR':
            func.LINEAR(param[1], duration, fs, use)
        elif param[0] == 'INVLINEAR':
            func.INVLINEAR(param[1], duration, fs, use)
        elif param[0] == 'EXP':
            func.EXP(param[1], duration, fs, use)
        elif param[0] == 'INVEXP':
            func.INVEXP(param[1], duration, fs, use)
        elif param[0] == 'QUARTCOS':
            func.QUARTCOS(param[1], duration, fs, use)
        elif param[0] == 'QUARTSIN':
            func.QUARTSIN(param[1], duration, fs, use)
        elif param[0] == 'HALFCOS':
            func.HALFCOS(param[1], duration, fs, use)
        elif param[0] == 'HALFISN':
            func.HALFSIN(param[1], duration, fs, use)
        elif param[0] == 'LOG':
            func.LOG(param[1], duration, fs, use)
        elif param[0] == 'INVLOG':
            func.INVLOG(param[1], duration, fs, use)
        elif param[0] == 'SIN':
            func.SIN(param[1], param[2], duration, fs, use)
        elif param[0] == 'TRI':
            func.TRI(param[1], param[2], param[3], duration, fs, use)
        elif param[0] == 'PULSES':
            func.PULSES(param[1], param[2], param[3], duration, fs, use)
        else:
            raise AssertionError('The given function is non-existant.')
        return func
    

def get_instrument(instrument) -> list:
    data = []
    with open(f"instruments/{instrument}", 'r') as ins:
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