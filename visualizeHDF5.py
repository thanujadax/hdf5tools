import pylab
import h5py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# inputFileName = '/home/thanuja/projects/data/drosophilaLarva_ssTEM/dataset01_hdf5/train/raw/00.hdf5'
inputFileName = '/home/thanuja/projects/external/gala/tests/example-data/train-ws.lzf.h5'
# inputFileName = 'file1.h5'

with h5py.File(inputFileName) as f:
    listItems = f.items()
    print 'List of items:',listItems
    for grp in listItems:
        print 'Group name:', grp[0]
        gp = f.get(grp[0])
        gpItems = gp.items()
        dsName = gpItems[0][0]
        print 'Dataset name:', dsName
        DS = gp.get(dsName)
        np_data = np.array(DS)
        plt.imshow(np_data, interpolation='nearest')
        plt.show()
        #img = Image.fromarray(np_data,'L')
        #img.save('imout.png')
        '''
            for DS in f: 
                # data = f[DS][:]
                print DS, "-->",f[DS]
                #data = f.get(DS)
                #np_data = np.array(data)
                #print 'Shape of the array ds1:', np_data.shape
                # pylab.plot(np_data)
                # pylab.show()
                # plt.plot(np_data)
                # plt.show()
        '''
