
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from brussel_stoch import simulate_brussel
import pytest

def test_main():

    # Simulation parameters
    Y1_init = 1000
    Y2_init = 2000
    k1 = 5000
    k2 = 50
    k3 = 0.00005
    k4 = 5
    t_initial = 0
    t_final = 10

    # Run simulation
    t_points, Y1_values, Y2_values = simulate_brussel(Y1_init, Y2_init, k1, k2, k3, k4, t_initial, t_final)

    # Time series plot
    plt.plot(t_points, Y1_values, label='Y1 (Prey)')
    plt.plot(t_points, Y2_values, label='Y2 (Predator)')
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Brusselator Model")
    plt.legend(loc="upper right")
    plt.savefig('brusselStoch_plot.png')
    plt.close()

    # Phase plot
    plt.plot(Y2_values, Y1_values)
    plt.xlabel("Y2 (Predator)")
    plt.ylabel("Y1 (Prey)")
    plt.title("Phase Plot: Y2 vs. Y1")
    plt.savefig( 'phase_plot.png')
    plt.close()

  
    
