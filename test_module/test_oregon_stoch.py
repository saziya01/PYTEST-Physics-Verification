
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from oregon_stoch import simulate_oregon
import pytest

def test_main():

    Y1_init = 500
    Y2_init = 1000
    Y3_init = 200
    k1 = 2
    k2 = 0.1
    k3 = 104
    k4 = 0.016
    k5 = 26
    t_initial = 0
    t_final = 3

# Run simulation
    t_points, Y1_values, Y2_values, Y3_values = simulate_oregon(Y1_init, Y2_init,Y3_init, k1, k2, k3,k4,k5, t_initial, t_final)

# Time series plot
    plt.plot(t_points, Y1_values, label='Y1 (Prey)')
    plt.plot(t_points, Y2_values, label='Y2 (Predator)')
    plt.plot(t_points, Y3_values, label='Y3 (Predator)')
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Oregonator Model")
    plt.legend()
    
    plt.savefig('OregonatorStoch_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as OregonatorStoch_plot.png")


# Phase plot
    plt.plot(Y2_values, Y1_values)
    plt.xlabel("Y2 (Predator)")
    plt.ylabel("Y1 (Prey)")
    plt.title("Phase Plot: Y2 vs. Y1")
    
    plt.savefig('OregonStochPhase_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as OregonStochphase_plot.png")

    
if __name__ == "__main__":
    test_main()
 
    
