# hdf5 tutorial

Official documentation for h5py:
http://docs.h5py.org/en/latest/high/group.html

HDF5 is made of dictionaries
An HDF5 file is organized in groups. 
Groups contain datasets or subgroups(=groups)
When it contains a dataset, the group is essentially a python dictionary
dataset name is key, array is value


## to get all keys in a dictionary into a list
```python
listOfKeys = list(Dictionary)
```

```python
for Key in Dictionary:
    print Key, "-->", Dictionary[Key]
```

## h5py module
To access the array stored in each dataset of an hdf5 file:

```python
import h5py

in_fid = h5py.File('inputFileName.h5','r')
for DS in in_fid:
    print DS, "-->",in_fid[DS]
```

`in_fid[DS]`: prints some meta information about the dataset DS

`in_fid[DS][...]`: prints the array values of that dataset

## Reading data:
open hdf5 file
extract a dataset
read the data
make an interactive plot
close file

```python
import pylab
import h5py

with h5py.File('inputFile.h5') as f:
    data = f['DSname'][:]
    pylab.plot(data)
    pylab.show()
```

# Creating files
```python
f = h5py.File('filename.hdf5','w')
```


