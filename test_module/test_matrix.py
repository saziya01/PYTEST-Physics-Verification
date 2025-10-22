import pytest
import numpy as np
from matrix import add_matrices, subtract_matrices, multiply_matrices, diagonalize_matrix

def test_add_matrices():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(A, B) == expected

def test_subtract_matrices():
    A = [[5, 6], [7, 8]]
    B = [[1, 2], [3, 4]]
    expected = [[4, 4], [4, 4]]
    assert subtract_matrices(A, B) == expected

def test_multiply_matrices():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert multiply_matrices(A, B) == expected

def test_diagonalize_matrix():
    A = [[4, 1], [2, 3]]
    eigenvalues, eigenvectors = diagonalize_matrix(A)
    expected_eigenvalues = [5, 2]
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))

if __name__ == "__main__":
    pytest.main()
