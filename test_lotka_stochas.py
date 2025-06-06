import pytest
import matplotlib.pyplot as plt

from lotka_stochas import simulate_lotkast


def test_main():
   Y1_init= 1000  # Prey population
   Y2_init= 1000  # Predator population

# Rate constants for the reactions 
   k1 = 10    # Natural growth rate of Y1
   k2 = 0.01  # Rate at which Y1 and Y2 interact
   k3 = 10    # Natural death rate of Y2
   t_initial= 0
   t_final = 10
  
 
   t_points, Y1_values, Y2_values = simulate_lotkast(Y1_init, Y2_init, k1, k2, k3,t_initial,t_final)
   plt.plot(t_points, Y1_values, label='Y1 (Prey)')
   plt.plot(t_points, Y2_values, label='Y2 (Predator)') 
   plt.xlabel("Time")
   plt.ylabel("Population")
   plt.title("Lotka-Volterra Model")
   plt.legend()
   plt.show()

# Phase plot: Y2 vs. Y1
   plt.plot(Y2_values, Y1_values)
   plt.xlabel("Y2 (Predator)")
   plt.ylabel("Y1 (Prey)")
   plt.title("Phase Plot: Y2 vs. Y1")
   plt.show()
   
