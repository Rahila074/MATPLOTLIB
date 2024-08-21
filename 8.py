#format string fmt
#you can also use the shortcut string natation parameter
#to specify the marker.
#this parameter is also called fmt,and is written with this sytax:
#sytax
#marker| line | color
#mark each poit with a circle
import matplotlib.pyplot as plt

import numpy as np


ypoints = np.array([3,8,1,10])
plt.plot( ypoints,'o:r')

plt.show()