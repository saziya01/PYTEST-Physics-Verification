import math
import random
import matplotlib.pyplot as plt

# Lotka Model Reactions
 
#   Y1 ------>  2Y1                       #  Prey Reproduction

#   Y1 + Y2 ------> Y1 + Y2              #  Predation

#   Y2 ------> ∅                         #  Predator Mortality



def simulate_lotkast(Y1_init,Y2_init,k1,k2,k3,t_initial,t_final):
    Y1 = Y1_init
    Y2 = Y2_init
   
    t_points = [t_initial]
    Y1_values = [Y1]
    Y2_values = [Y2]
  

    while t_initial < t_final and (Y1 > 0 or Y2 > 0):
    # Calculate propensity functions
      a1 = k1 * Y1  # Rate of Y1 birth
      a2 = k2 * Y1 * Y2  # Rate of Y1 and Y2 interaction
      a3 = k3 * Y2  # Rate of Y2 death
      a0 = a1 + a2 + a3  # Total rate

    # Generate random numbers for stochastic simulation
      r1 = random.uniform(0, 1)
      if a0 > 0:
         tau = (1 / a0) * math.log(1 / r1)  # Time step
      else:
         tau = float('inf')  # No event if total rate is zero

    # Update time
      t_initial += tau

    # Generate another random number to determine the event
      r2 = random.uniform(0, 1)

    # Determine which event occurs based on r2
      if r2 * a0 < a1:
        Y1 += 1  # Y1 reproduces
      elif r2 * a0 < a1 + a2:
        Y2 += 1  # Y2 reproduces
        Y1 -= 1  # Y1 is consumed
      elif r2 * a0 < a1 + a2 + a3:
        Y2 -= 1  # Y2 dies

    # Record the new state
      t_points.append(t_initial)
      Y1_values.append(Y1)
      Y2_values.append(Y2)

    return t_points, Y1_values, Y2_values
