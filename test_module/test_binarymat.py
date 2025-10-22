import numpy as np
import pytest
from binary_matrix import (
    generate_random_matrix,
    save_matrix_to_hdf5,
    read_matrix_from_hdf5
)

def test_display_and_compress_matrices():
    # Generate two random 3x3 matrices
    matrix1 = generate_random_matrix()
    matrix2 = generate_random_matrix()

    # Display the original matrices
    print("Original Matrix 1:")
    print(matrix1)

    print("\nOriginal Matrix 2:")
    print(matrix2)

    # Save with gzip compression level 2
    save_matrix_to_hdf5('matrix1.h5', 'dataset1', matrix1, compression_level=2)
    save_matrix_to_hdf5('matrix2.h5', 'dataset2', matrix2, compression_level=2)

    # Read and print the matrices back from the compressed HDF5 files
    loaded1 = read_matrix_from_hdf5('matrix1.h5', 'dataset1')
    loaded2 = read_matrix_from_hdf5('matrix2.h5', 'dataset2')

    print("\nCompressed Matrix 1 (Read from file):")
    print(loaded1)

    print("\nCompressed Matrix 2 (Read from file):")
    print(loaded2)

    # Assert to verify the saved and loaded matrices are the same
    assert np.allclose(matrix1, loaded1), "Matrix 1 mismatch after compression"
    assert np.allclose(matrix2, loaded2), "Matrix 2 mismatch after compression"

if __name__ == '__main__':
    test_display_and_compress_matrices()
