 
import math 
import random 

def simulate_oregon(Y1_init,Y2_init,Y3_init,k1,k2,k3,k4,k5,t_initial,t_final):
    Y1 = Y1_init
    Y2 = Y2_init
    Y3 = Y3_init
    
    t_points = [t_initial]
    Y1_values = [Y1]
    Y2_values = [Y2]
    Y3_values = [Y3]
    
    while t_initial<t_final and (Y1>0 or Y2>0):
    
        a1 = k1*Y2
        a2 = k2*Y1*Y2
        a3 = k3*Y1
        a4 = k4*(Y1*(Y1-1)/2)
        a5 = k5*Y3
        a0 = a1+a2+a3+a4+a5
# generate random number

        r1 = random.uniform(0,1)

        if a0 > 0: 
            tau = (1/a0)*math.log(1/r1)
        else:
            tau = float('inf')
        t_initial += tau 
        r2 = random.uniform(0,1)
        if  a0*r2 < a1 :
            Y1 = Y1+1
            Y2 = Y2 -1
        elif  a0*r2 < (a1+a2) :
            Y2 = Y2 - 1 
            Y1 = Y1 - 1  
        elif a0*r2 < (a1+a2+a3):
            Y1= Y1+1
            Y3 = Y3 + 1
        elif a0*r2<(a1+a2+a3+a4):
            Y1 = Y1-2
        elif   a0*r2<(a1+a2+a3+a4+a5):
            Y3 = Y3 - 1
            Y2 = Y2 +1 
    
        t_points.append(t_initial)
        Y1_values.append(Y1)
        Y2_values.append(Y2)
        Y3_values.append(Y3)
    return t_points,Y1_values,Y2_values,Y3_values

    
