
import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt


def equations(y,t,k1,k2,k3,k4,k5):
     
    y1, y2, y3 = y 
    
    dy1dt = k1*y2 - k2*y1*y2 + k3*y1 - 2*(k4/2)*y1*y1 
    dy2dt = -k1*y2 - k2*y2*y1 + k5*y3 
    dy3dt = k3*y1 - k5*y3 
    
    return(dy1dt, dy2dt, dy3dt) 
def simulate_oreg(y1,y2,y3,k1,k2,k3,k4,k5,t_range):
    y0=[y1,y2,y3]
    t = np.linspace(*t_range)
    
    sol = intgr.odeint(equations, y0 , t, args=(k1, k2,k3,k4,k5))
    return t,sol
