import pytest
import numpy as np
from ising_model import (
    calculate_energy,
    calculate_magnetization,
    run_ising_simulation,
    plot_results
)

@pytest.fixture
def spins_all_up():
    return np.ones(10, dtype=int)

@pytest.fixture
def spins_alternating():
    return np.array([1, -1] * 5)

@pytest.fixture
def spins_all_down():
    return -np.ones(10, dtype=int)

@pytest.fixture
def spins_half_up_half_down():
    return np.array([1, -1] * 5)

@pytest.mark.parametrize("spins, expected", [
    (np.ones(10, dtype=int), -10.0),
    (np.array([1, -1] * 5), 10.0)
])
def test_calculate_energy(spins, expected):
    assert np.isclose(calculate_energy(spins, J=1), expected)

def test_calculate_magnetization_all_down(spins_all_down):
    assert np.isclose(calculate_magnetization(spins_all_down), 1.0)

def test_calculate_magnetization_half_up_half_down(spins_half_up_half_down):
    assert np.isclose(calculate_magnetization(spins_half_up_half_down), 0.0)

def test_run_ising_simulation_output_keys():
    result = run_ising_simulation(N=10, MCS=100, temperature_range=np.linspace(1, 2, 3))
    expected_keys = {
        "temperature_range", "average_energies", "average_magnetizations",
        "specific_heats", "magnetic_susceptibility"
    }
    assert expected_keys.issubset(result.keys())

def test_run_ising_simulation_output_lengths():
    T_range = np.linspace(1, 2, 5)
    result = run_ising_simulation(N=10, MCS=100, temperature_range=T_range)
    for key in ["average_energies", "average_magnetizations", "specific_heats", "magnetic_susceptibility"]:
        assert len(result[key]) == len(T_range)

def test_plot_results():
    T_range = np.linspace(0.1, 5, 50)
    result = run_ising_simulation(N=50, MCS=500, temperature_range=T_range)
    plot_results(result)  # This will open plots; typically not included in unit tests
