import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt

# Lotka Model Reactions
 
#   Y1 ------>  2Y1                            #  Prey Reproduction

#   Y1 + Y2 ------> Y1 + Y2                    #  Predation

#   Y2 ------> ∅                               #  Predator Mortality

# Define the system of differential equations


def equations(x, t, k1, k2, k3):  
    y1, y2 = x  # Unpack the variables
    dy1dt = k1 * y1 - k2 * y1 * y2              # Rate equation for y1
    dy2dt = k2 * y1 * y2 - k3 * y2              # Rate equation for y2
    
    return [dy1dt, dy2dt]
def simulate_lotka(y1,y2,k1,k2,k3,time):
    init = [y1,y2]
    T = 15.0                                        # Total simulation time
    time = np.linspace(0, 10, 1000)
    sol = intgr.odeint(equations, init, time, args=(k1, k2, k3))
    return time,sol
