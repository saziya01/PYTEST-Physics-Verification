
import numpy as np
from scipy import integrate as intgr

# Define the system of differential equations
def equations(X, t, k1, k2, m1, m2, m3):
    x1, x2, x3, v1, v2, v3 = X

    dx1 = v1
    dx2 = v2
    dx3 = v3

    dv1 = -(k1/m1) * (x1 - x2)
    dv2 = -(k1/m2) * (x2 - x1) - (k2/m2) * (x2 - x3)
    dv3 = -(k2/m3) * (x3 - x2)

    return [dx1, dx2, dx3, dv1, dv2, dv3]

# Function to build and analyze the system matrix
def compute_eigenvalues(k1, k2, m1, m2, m3):
    # Construct the matrix A for normal mode analysis
    A = np.array([
        [-(k1/m1),     k1/m1,          0     ],
        [k1/m2,  -(k1+k2)/m2,     k2/m2 ],
        [0,         k2/m3,      -k2/m3 ]
    ])

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Convert eigenvalues to frequencies (imaginary parts)
    frequencies = np.sqrt(np.abs(eigenvalues))

    return eigenvalues, eigenvectors, frequencies

# Wrapper to solve the coupled oscillator system
def coupleosc(X, V, k1, k2, m1, m2, m3, t_range):
    x1i, x2i, x3i = X
    v1i, v2i, v3i = V
    init = [x1i, x2i, x3i, v1i, v2i, v3i]

    t = np.linspace(*t_range)
    sol = intgr.odeint(equations, init, t, args=(k1, k2, m1, m2, m3))

    return t, sol