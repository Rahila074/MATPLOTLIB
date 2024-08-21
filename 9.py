#marker size

#you can use the keyword argument marker size
#or the shorter version , ms to set the size of the markers:
#set the size of the markers to 20?

import matplotlib.pyplot as plt

import numpy as np


ypoints = np.array([3,8,1,10])
plt.plot( ypoints,marker='o',ms=20)

plt.show()
