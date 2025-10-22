import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pytest
from coupled_oscillator  import coupleosc, compute_eigenvalues

def test_main():
    # Collect user input
    x1i = 0.0
    x2i = 0.2
    x3i = 0.4

    v1i = 0
    v2i = 0
    v3i = 0

    m1 = 1
    m2 = 2
    m3 = 1

    k1 = 1.0
    k2 = 1.5
    t_range = (0, 50, 1000)  # (start, stop, number of points)

    # Solve the system
    t, sol = coupleosc((x1i, x2i, x3i), (v1i, v2i, v3i), k1, k2, m1, m2, m3, t_range)

    x1 = sol[:, 0]
    x2 = sol[:, 1]
    x3 = sol[:, 2]

    # Plot oscillator waves
    plt.figure(figsize=(10, 6))
    plt.plot(t, x1, label='Mass 1')
    plt.plot(t, x2, label='Mass 2')
    plt.plot(t, x3, label='Mass 3')
    plt.title("Coupled Oscillator Displacements")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement")
   # plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('Coupled_Oscillator_plot.png')
    plt.close()
    # Compute and print eigen data
    eigvals, eigvecs, freqs = compute_eigenvalues(k1, k2, m1, m2, m3)

    print("\nEigenvalues:")
    print(eigvals)
    print("\nEigenvectors (columns = normal modes):")
    print(eigvecs)
    print("\nFrequencies (rad/s):")

if __name__ == "__main__":
   test_main()                    
