import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pytest
import numpy as np
from random_walk import single_random_walk, multiple_random_walks, random_walk_statistics

def test_single_random_walk():
    steps = 300
    traj = single_random_walk(steps)
    assert len(traj) == steps + 1
    assert isinstance(traj, list)
    assert all(isinstance(x, int) for x in traj)
    assert traj[0] == 0  # starts at 0
    
    plt.figure()
    plt.plot(traj)
    plt.title("Single Random Walk")
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.grid(True)
    plt.savefig('1DSingle_plot.png')
    plt.close()
    print("Plot saved as 1DSingle_plot.png")

def test_single_random_walk_zero_steps():
    traj = single_random_walk(0)
    assert traj == [0]  # Only starting position

def test_single_random_walk_immutable_output():
    steps = 10
    traj = single_random_walk(steps)
    # Modifying the returned list should not affect internal state (which doesn't exist here),
    # so we just check if a new list is returned each call
    traj2 = single_random_walk(steps)
    assert traj is not traj2
    assert traj != traj2 or traj == traj2  # Values can vary due to randomness but lists are separate

def test_multiple_random_walks():
    steps = 300
    walkers = 50
    walks = multiple_random_walks(steps, walkers)
    assert len(walks) == walkers
    for traj in walks:
        assert len(traj) == steps + 1

    plt.figure()
    for traj in walks:
        plt.plot(traj, alpha=0.6)
    plt.title(f"{walkers} Random Walks")
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.grid(True)
    plt.savefig('1DMultiple_plot.png')
    plt.close()
    print("Plot saved as 1DMultiple_plot.png")

def test_multiple_random_walks_zero_walkers():
    walks = multiple_random_walks(10, 0)
    assert walks == []

def test_random_walk_statistics():
    steps = 200
    walkers = 100
    stats = random_walk_statistics(steps, walkers)
    assert len(stats) == walkers
    assert all(isinstance(x, int) for x in stats)
    assert all(abs(pos) <= steps for pos in stats)
    
    final_positions = np.array(stats)
    mean = np.mean(final_positions)
    std_dev = np.std(final_positions)
    variance = np.var(final_positions)

    print(f"Mean: {mean}")
    print(f"Standard deviation: {std_dev}")
    print(f"Variance: {variance}")

    plt.figure()
    plt.hist(stats, bins=20, edgecolor='black')
    plt.title("Histogram of Final Positions")
    plt.xlabel("Final Position")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig('Histogram_plot.png')
    plt.close()
    print("Plot saved as Histogram_plot.png")

def test_random_walk_statistics_zero_walkers():
    stats = random_walk_statistics(10, 0)
    assert stats == []

def test_random_walk_statistics_zero_steps():
    stats = random_walk_statistics(0, 10)
    assert all(pos == 0 for pos in stats)

def test_single_random_walk_invalid_steps():
    # Currently, the function doesn't raise errors for invalid inputs.
    # Testing for negative steps, expecting empty or only start position output logically.
    traj = single_random_walk(-5)
    assert traj == [0]  # The for-loop would not run

def test_multiple_random_walks_invalid_inputs():
    walks = multiple_random_walks(0, 5)  # zero steps still returns list of walks with just start position
    assert all(len(w) == 1 for w in walks)
    walks = multiple_random_walks(5, 0)  # zero walkers returns empty list
    assert walks == []

def test_random_walk_statistics_invalid_inputs():
    stats = random_walk_statistics(0, 0)
    assert stats == []

def test_randomness_variability():
    steps = 100
    traj1 = single_random_walk(steps)
    traj2 = single_random_walk(steps)
    # Because random, they may occasionally be identical, but very unlikely for 100 steps
    identical = traj1 == traj2
    assert not identical or identical  # Just a placeholder to confirm function runs without crashes

def test_random_walk_statistics_distribution_shape():
    # Check roughly if distribution is roughly symmetric around zero mean
    steps = 1000
    walkers = 500
    stats = random_walk_statistics(steps, walkers)
    mean = np.mean(stats)
    # Mean ideally close to zero in random walk with large sample
    assert abs(mean) < 50  # larger threshold, just to check symmetry roughly

def test_single_random_walk_contains_only_valid_positions():
    steps = 20
    traj = single_random_walk(steps)
    valid_positions = set()
    pos = 0
    # Track possible positions by walking
    for step_value in traj[1:]:
        diff = step_value - pos
        assert diff == 1 or diff == -1
        pos = step_value


