import numpy as np
import os
import pytest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from radioactive_decay import simulate_decay

def test_initial_conditions():
    A0 = 100
    B0 = 0
    k = 0.1
    t_range = (0, 50, 1000)

    t, sol = simulate_decay(A0, B0, k, t_range)

    # Check initial conditions
    assert np.isclose(sol[0, 0], A0), "Initial amount of A should be A0"
    assert np.isclose(sol[0, 1], B0), "Initial amount of B should be B0"

def test_decay_behavior():
    A0 = 100
    B0 = 0
    k = 0.1
    t_range = (0, 50, 1000)

    t, sol = simulate_decay(A0, B0, k, t_range)

    # Check that A decreases over time
    assert sol[-1, 0] < A0, "Amount of A should decrease over time"
    # Check that B increases over time
    assert sol[-1, 1] > B0, "Amount of B should increase over time"

def test_decay_rate():
    A0 = 100
    B0 = 0
    k = 0.1
    t_range = (0, 50, 1000)

    t, sol = simulate_decay(A0, B0, k, t_range)

    # Check that the decay follows the expected exponential decay
    expected_A = A0 * np.exp(-k * t)
    assert np.allclose(sol[:, 0], expected_A, rtol=1e-2), "Decay of A does not match expected exponential decay"

def test_plot_saving():
    A0 = 100
    B0 = 0
    k = 0.1
    t_range = (0, 50, 1000)

    t, sol = simulate_decay(A0, B0, k, t_range)

    plt.plot(t, sol[:, 0])
    plt.plot(t, sol[:, 1])
    plt.xlabel('Time (t)')
    plt.ylabel('Number of molecules')
    plt.title('Radioactive Decay Simulation')
    plt.grid()
   
    plt.savefig('radioactive_decay_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory

    # Check if the plot file was created
    assert os.path.exists('radioactive_decay_plot.png'), "Plot file was not created"

if __name__ == "__main__":
    pytest.main()
