import numpy as np
import pytest
from pot_well import psi_superposition, normalize_wavefunction, probability_in_half

@pytest.fixture
def setup_domain():
    L = 1.0
    x = np.linspace(0, L, 1000)
    dx = x[1] - x[0] 
    return x, dx, L

def test_wavefunction_superposition_shape(setup_domain):
    x, dx, L = setup_domain 
    psi_vals = psi_superposition(x, L) 
    assert psi_vals.shape == x.shape, "Wavefunction shape mismatch with spatial domain."

def test_wavefunction_normalization(setup_domain):
    x, dx, L = setup_domain
    psi_vals = psi_superposition(x, L)
    normed = normalize_wavefunction(psi_vals, dx)
    total_prob = np.sum(np.abs(normed)**2) * dx
    assert np.isclose(total_prob, 1.0, atol=1e-3), "Wavefunction not normalized properly."

def test_probability_left_half(setup_domain):
    x, dx, L = setup_domain
    psi_vals = psi_superposition(x, L)
    normed = normalize_wavefunction(psi_vals, dx)
    prob_left_half = probability_in_half(normed, dx)
    expected = 0.924413
    assert np.isclose(prob_left_half, expected, atol=0.01), f"Expected {expected}, got {prob_left_half}"

def test_wavefunction_zero_norm_raises_error():
    zero_wave = np.zeros(1000)
    dx = 0.001
    with pytest.raises(ValueError, match="Wavefunction norm is zero"):
        normalize_wavefunction(zero_wave, dx)

def test_probability_bounds(setup_domain):
    x, dx, L = setup_domain
    psi_vals = psi_superposition(x, L)
    normed = normalize_wavefunction(psi_vals, dx)
    prob_left = probability_in_half(normed, dx)
    assert 0 <= prob_left <= 1, "Probability must be between 0 and 1."
