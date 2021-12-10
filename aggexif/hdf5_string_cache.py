import os

import h5py


class HDF5StringCache:
    def __init__(self, file_name, group_name):
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        self.h5 = h5py.File(file_name, 'a')
        self.group = self.h5.require_group(group_name)
        self.file_name = file_name
        self.group_name = group_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def add(self, name: str, value: str):
        dataset = self.group.require_dataset(name, shape=(1,), dtype=h5py.string_dtype())
        dataset[0] = value

    def read(self, name: str):
        dataset = self.group.get(name)
        return dataset and dataset[0]

    def close(self):
        self.h5.close()
