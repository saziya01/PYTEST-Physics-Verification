# test_estimate_pi.py

import pytest
from estimate_pi import estimate_pi
import math

# Test Suite for Pi Estimation
class TestPiEstimation:

    def test_basic_accuracy(self):
        """Test estimate with a reasonably large sample."""
        num_samples = 100_000
        estimated = estimate_pi(num_samples)
        assert math.isclose(estimated, math.pi, rel_tol=0.01)

    def test_low_sample_accuracy(self):
        """Check rough correctness with fewer samples."""
        num_samples = 1_000
        estimated = estimate_pi(num_samples)
        assert 2.5 < estimated < 3.8  # loose bounds due to randomness

    def test_zero_samples(self):
        """Ensure exception is raised for zero samples."""
        with pytest.raises(ValueError, match="Number of samples must be greater than zero."):
            estimate_pi(0)

    def test_negative_samples(self):
        """Ensure exception is raised for negative samples."""
        with pytest.raises(ValueError, match="Number of samples must be greater than zero."):
            estimate_pi(-100)
