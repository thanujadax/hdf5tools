import h5py
import numpy as np

f = h5py.File('filename.hdf5','w')

m1 = np.random.random(size=(1000,20))
m2 = np.random.random(size=(1000,20))


with h5py.File('file1.h5','w') as hf:
    hf.create_dataset('ds1', data=m1)
    #hf.create_dataset('ds2', data=m2)
