#marker colour

#you can use the key word argument marker edge color
#or the shorter mec to set the colour of the edge of the markers :
#set the EDGE color to red

import matplotlib.pyplot as plt

import numpy as np


ypoints = np.array([3,8,1,10])
plt.plot( ypoints,marker='o',ms=20,mec='r')

plt.show()
