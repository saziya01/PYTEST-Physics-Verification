import h5py
import numpy as np

def generate_random_matrix(shape=(3, 3)):
    return np.random.random(shape)

def save_matrix_to_hdf5(filename, dataset_name, data, compression_level=9):
    with h5py.File(filename, 'w') as f:
        f.create_dataset(
            dataset_name,
            data=data,
            compression='gzip',
            compression_opts=compression_level
        )

def read_matrix_from_hdf5(filename, dataset_name):
    with h5py.File(filename, 'r') as f:
        return f[dataset_name][:]
