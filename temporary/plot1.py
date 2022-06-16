import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y = np.linspace(20, 40, 100)
z = np.linspace(40, 60, 100)
plt.plot(x, 800 * np.sin(x))
plt.plot(y, 800 * np.cos(y))
plt.plot(z, np.tan(z))
plt.show()

def 


