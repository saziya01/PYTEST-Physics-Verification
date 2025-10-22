 
import math 
import random 

def simulate_brussel(Y1_init,Y2_init,k1,k2,k3,k4,t_initial,t_final):
    Y1 = x1 = Y1_init
    Y2 = x2 = Y2_init
    
    t_points = [t_initial]
    Y1_values = [Y1]
    Y2_values = [Y2]
    
    while t_initial < t_final and (Y1 > 0 or Y2 > 0):
    
    # Calculate propensity functions (reaction rates)
        a1 = k1  # Constant production of Y1
        a2 = k2 * Y1  # Conversion of Y1 to Y2
        a3 = k3 * (Y1 * (Y1 - 1) / 2) * Y2  # Nonlinear reaction involving Y1 and Y2
        a4 = k4 * Y1  # Degradation of Y1
        a0 = a1 + a2 + a3 + a4  # Total propensity sum
    
     # Generate a random number for time step
        r1 = random.uniform(0, 1)
        if a0 > 0: 
            tau = (1 / a0) * math.log(1 / r1)  # Time increment based on reaction rates
        else:
            tau = float('inf')  # No more reactions possible
  
        t_initial += tau  # Update time
    
    # Generate another random number to decide which reaction occurs
        r2 = random.uniform(0, 1)
 
    # Determine which reaction occurs based on cumulative probabilities
        if a0 * r2 < a1:
            x1 = x1 - 1  # Decrease x1 count
            Y1 = Y1 + 1  # Increase Y1 count (production)
        elif a0 * r2 < (a1 + a2):
            x2 = x2 - 1  # Decrease x2 count
            Y1 = Y1 - 1  # Decrease Y1 count
            Y2 = Y2 + 1  # Increase Y2 count
        elif a0 * r2 < (a1 + a2 + a3):
            Y2 = Y2 - 1  # Decrease Y2 count
            Y1 = Y1 + 1  # Increase Y1 count
        elif a0 * r2 < (a1 + a2 + a3 + a4):
            Y1 = Y1 - 1  # Decrease Y1 count due to degradation
 
    # Store updated values for plotting
        t_points.append(t_initial)
        Y1_values.append(Y1)
        Y2_values.append(Y2)
    return t_points,Y1_values,Y2_values
