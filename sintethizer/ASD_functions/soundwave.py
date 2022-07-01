import numpy as np
import matplotlib.pyplot as plt
from functions import Function

def main(instrument):
    waves = {}
    with open(f"instruments/{instrument}", 'r') as ins:
        harmonics = int(ins.readline())
        for i in range(harmonics):
            line = (ins.readline()).rstrip('\n')
            line = line.split(' ')
            waves[int(line[0])] = float(line[1])
        return waves
            
            
if __name__ == "__main__":
    main("piano.txt")
    