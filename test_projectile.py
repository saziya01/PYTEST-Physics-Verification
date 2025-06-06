import pytest
import math
from projectile import calculate_range

#  Parametrized test for multiple valid inputs
@pytest.mark.parametrize("v, angle, expected", [
    (0, 45, 0),
    (10, 0, 0),
    (10, 45, (10**2) * math.sin(math.radians(90)) / 9.81),
    (20, 30, (20**2) * math.sin(math.radians(60)) / 9.81)
])
def test_calculate_range_valid(v, angle, expected):
    assert calculate_range(v, angle) == pytest.approx(expected, rel=1e-3)


#  Test for exception: negative velocity
def test_negative_velocity():
    with pytest.raises(ValueError, match="Velocity cannot be negative"):
        calculate_range(-10, 45)


#  Test for exception: invalid angles
@pytest.mark.parametrize("angle", [-10, 100])
def test_invalid_angle(angle):
    with pytest.raises(ValueError, match="Angle must be between 0 and 90 degrees"):
        calculate_range(10, angle)


#  Fixture for common test values
@pytest.fixture
def common_params():
    return {
        "v": 15,
        "theta": 60,
        "expected": (15**2) * math.sin(math.radians(120)) / 9.81
    }

def test_with_fixture(common_params):
    result = calculate_range(common_params["v"], common_params["theta"])
    assert result == pytest.approx(common_params["expected"], rel=1e-3)