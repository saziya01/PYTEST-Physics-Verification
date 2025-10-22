# estimate_pi.py

import random

def estimate_pi(num_samples):
    """
    Estimate the value of Pi using the Monte Carlo method.

    Parameters:
    - num_samples (int): Number of random samples to use.

    Returns:
    - float: Approximated value of Pi.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4
