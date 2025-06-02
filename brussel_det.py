import numpy as np
import scipy.integrate as intgr 
import matplotlib.pyplot as plt  

def equations(y,t,k1,k2,k3,k4): 
    
    #k1, k2, k3, k4 = 5000,50,0.00005,5
    y1, y2 = y  
    dy1dt = k1 - k2 * y1 + (k3 / 2) * y1 * y1 * y2 - k4 * y1
    dy2dt = k2 * y1 - (k3 / 2) * y1 * y1 * y2

    return [dy1dt, dy2dt]

def simulate_brussel(y1,y2,k1,k2,k3,k4,t_range):
    y0 = [y1,y2] 
    t = np.linspace(*t_range)
    sol = intgr.odeint(equations, y0 , t, args=(k1, k2,k3,k4))
    return t, sol
