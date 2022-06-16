import numpy as np
import matplotlib.pyplot as plt
from asdbis import Function
from pathlib import Path


# def get_func(param: list, duration, fs):
#     if param[0] == 'CONSTANT':
#         func = asd.CONSTANT(duration, 1/fs)
#     elif param[0] == 'LINEAR':
#         func = asd.LINEAR(param[1], duration, 1/fs)
#     elif param[0] == 'INVLINEAR':
#         func = asd.INVLINEAR(param[1], duration, 1/fs)
#     elif param[0] == 'EXP':
#         func = asd.EXP(param[1], duration, 1/fs)
#     elif param[0] == 'INVEXP':
#         func = asd.INVEXP(param[1], duration, 1/fs)
#     elif param[0] == 'QUARTCOS':
#         func = asd.QUARTCOS(param[1], duration, 1/fs)
#     elif param[0] == 'QUARTSIN':
#         func = asd.QUARTSIN(param[1], duration, 1/fs)
#     elif param[0] == 'HALFCOS':
#         func = asd.HALFCOS(param[1], duration, 1/fs)
#     elif param[0] == 'HALFISN':
#         func = asd.HALFSIN(param[1], duration, 1/fs)
#     elif param[0] == 'LOG':
#         func = asd.LOG(param[1], duration, 1/fs)
#     elif param[0] == 'INVLOG':
#         func = asd.INVLOG(param[1], duration, 1/fs)
#     elif param[0] == 'SIN':
#         func = asd.SIN(param[1], param[2], duration, 1/fs)
#     elif param[0] == 'TRI':
#         func = asd.TRI(param[1], param[2], param[3], duration, 1/fs)
#     elif param[0] == 'PULSES':
#         func = asd.PULSES(param[1], param[2], param[3], duration, 1/fs)
#     else:
#         return ValueError
#     return func

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