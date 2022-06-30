import numpy as np
from functions import Function
import matplotlib.pyplot as plt

def main():
    duration = 2
    freq = 440
    array = np.linspace(0, duration, freq * 15)
    function = Function()
    result = function.EXP(2, array)
    print(array)
    print(result)
    plt.plot(array, result)
    plt.show()

if __name__ == "__main__":
    main()