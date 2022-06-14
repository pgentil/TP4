import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

class Attack():
        
    def LINEAR(self, t0, dom, im):
        values = np.zeros(dom)
        for t in range(dom):
            if t / t0 < im:
                values[t] = t * t0
        return values
        
    
class Sustain():
    
    def CONSTANT(self, dom):
        return np.ones(dom)
    
    def INVLINEAR(self, t0, dom, im):
        values = np.zeros(dom)
        for t in range(dom):
            if max(1 - (t / t0)) < im:
                values[t] = (max(1 - (t / t0)))
        return values
    
    def SIN(self, a, f, dom, im):
        values = np.zeros(dom)
        for t in range(dom):
            if 1 + (a * np.sin(f * t)) < im:
                values[t] = 1 + (a * np.sin(f * t))
        return values
                
    
class Decay():
    
    def INVLINEAR(self, t0, dom, im):
        values = np.zeros(dom)
        for t in range(dom):
            if max(1 - (t / t0)) < im:
                values[t] = max(1 - (t / t0))
        return values