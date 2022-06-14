import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

class Attack():
        
    def LINEAR(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = t / t0
        return values
        
    def EXP(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.exp(5 * (t - t0) / t0)
        return values
    
    def QUARTSIN(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.sin((pi * t) / (2 * t0))
        return values
    
    def HALFSIN(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = (1 + np.cos(pi * (t / t0 - 0.5))) / 2
        return values
    
    def LOG(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.log10(9 * t / t0 + 1)
        return values
    
    def TRI(self, t0, t1, a1, dom):
        values = np.zeros(dom)
        for t in range(dom):
            if t < t1:
                values[t] = t * a1 / t1
            elif t > t1:
                values[t] = (t - t1) / (t1 - t0)
        return values
    
    
class Sustain():
    
    def CONSTANT(self, dom):
        return np.ones(dom)
    
    def INVLINEAR(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = (max(1 - (t / t0)))
        return values
    
    def SIN(self, a, f, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = 1 + (a * np.sin(f * t))
        return values
    
    def INVEXP(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.exp((-5 * t) / t0)
        return values
    
    def QUARTCOS(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.cos((pi * t) / (2 * t0))
        return values
    
    def HALFCOS(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = (1 + np.cos(pi * t / t0)) / 2
        return values
    
    def INVLOG(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            if t < t0:
                values[t] = np.log10((-9 * t) / t0 + 10)
            else:
                values[t] = 0
        return values
    
class Decay():
    
    def INVLINEAR(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = max(1 - (t / t0))
        return values
    
    def INVEXP(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.exp((-5 * t) / t0)
        return values
    
    def QUARTCOS(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = np.cos((pi * t) / (2 * t0))
        return values
    
    def HALFCOS(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            values[t] = (1 + np.cos(pi * t / t0)) / 2
        return values
    
    def INVLOG(self, t0, dom):
        values = np.zeros(dom)
        for t in range(dom):
            if t < t0:
                values[t] = np.log10((-9 * t) / t0 + 10)
            else:
                values[t] = 0
        return values