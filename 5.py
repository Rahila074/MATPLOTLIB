#multiple points
#you can plott as many points as you like,
#just make sure you have  the same number of points in both axisis.

#draw  a line in a diagram from position (1,3)to(2,8)
#then to (6,1) and finally to position(8,10):

import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])
plt.plot( xpoints,ypoints)
plt.show()


