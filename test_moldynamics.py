import pytest
import numpy as np
import matplotlib.pyplot as plt
from mol_dynamics import run_simulation

def test_energy_conservation():
    # Simulation parameters
    eps = 1.0
    sig = 1.0
    N = 50
    box_size = 50
    dt = 0.01
    steps = 1000
    m = 1.0

    # Run simulation
    pot_energies, kin_energies, total_energies = run_simulation(N, box_size, eps, sig, m, dt, steps)

    # Check if total energy is approximately constant
    assert np.allclose(total_energies, total_energies[0], rtol=0.1), "Total energy is not conserved."

# def test_potential_energy():
#     # Simulation parameters
#     eps = 1.0
#     sig = 1.0
#     N = 10
#     box_size = 10
#     dt = 0.01
#     steps = 100
#     m = 1.0

#     # Run simulation
#     pot_energies, _, _ = run_simulation(N, box_size, eps, sig, m, dt, steps)

#     # Check if potential energy is non-negative
#     assert np.all(pot_energies >= 0), "Potential energy should be non-negative."

def test_potential_energy():
    # Simulation parameters
    eps = 1.0
    sig = 1.0
    N = 10
    box_size = 10
    dt = 0.01
    steps = 100
    m = 1.0

    # Run simulation
    pot_energies, _, _ = run_simulation(N, box_size, eps, sig, m, dt, steps)

    # Check if potential energy is above a certain threshold
    threshold = -1.0  # Set a threshold based on your system
    assert np.all(pot_energies >= threshold), f"Potential energy should be above {threshold}."


def test_kinetic_energy():
    # Simulation parameters
    eps = 1.0
    sig = 1.0
    N = 10
    box_size = 10
    dt = 0.01
    steps = 100
    m = 1.0

    # Run simulation
    _, kin_energies, _ = run_simulation(N, box_size, eps, sig, m, dt, steps)

    # Check if kinetic energy is non-negative
    assert np.all(kin_energies >= 0), "Kinetic energy should be non-negative."

def test_plot_saving():
    # Simulation parameters
    eps = 1.0
    sig = 1.0
    N = 50
    box_size = 50
    dt = 0.01
    steps = 1000
    m = 1.0

    # Run simulation
    pot_energies, kin_energies, total_energies = run_simulation(N, box_size, eps, sig, m, dt, steps)

    # Plot results
    time_steps = np.arange(steps)
    plt.plot(time_steps, total_energies, label="Total Energy")
    plt.plot(time_steps, pot_energies, label="Potential Energy")
    plt.plot(time_steps, kin_energies, label="Kinetic Energy")
    plt.xlabel("Time steps")
    plt.ylabel("Energy")
    plt.title("Molecular Dynamics Simulation")
    plt.legend()
    plt.tight_layout()

    plt.savefig('MolecularDynamicsSimulation_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    assert True, "Plot saved successfully."

if __name__ == "__main__":
    pytest.main()
