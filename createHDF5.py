import h5py
from PIL import Image                                                            
import numpy                                                                     
import matplotlib.pyplot as plt                                                  
import glob

'''
import numpy as np
import os
from scipy import misc
'''

outputH5fileName = '/home/thanuja/projects/data/drosophilaLarva_ssTEM/dataset01_hdf5/train/test_gt.h5'

inputDir = '/home/thanuja/projects/data/toyData/set8/groundtruth';
imagePath = glob.glob(inputDir+'/*.tif') 

im_array = numpy.array( [numpy.array(Image.open(imagePath[i]).convert('L'), 'f') for i in range(0,9)] )

# uncomment the following line for probability maps s.t it is converted into probabilities [0,1]
# im_array = numpy.divide(im_array,255)

with h5py.File(outputH5fileName,'w') as hf:
    hf.create_dataset('stack',data=im_array)


'''
i = 0
sshape = (3,500,500)
npArray = np.zeros(sshape)
# read all files with tif extension
for file in sorted(os.listdir(inputDir)):
    if file.endswith(".tif"):
        print(file)
        # inssert file in numpy array. flatten=1 reads grayscale image
        npArray[i,:,:] = misc.imread(file,flatten=1)
        i = i+1
'''


'''
f = h5py.File('filename.hdf5','w')

m1 = np.random.random(size=(1000,20))
m2 = np.random.random(size=(1000,20))


with h5py.File('file1.h5','w') as hf:
    hf.create_dataset('ds1', data=m1)
    #hf.create_dataset('ds2', data=m2)
'''
