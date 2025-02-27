#combine color size and alpha
#you can combine a colormap with different size of the dots.
#this is best visualized if the dots are transperent :
#create random arrays with 100 values for x-points,y-points,
#color and sizes?

import matplotlib.pyplot as plt
import numpy as np

x =np.random.randint(100,size=(100))
y =np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=10*np.random.randint(100,size=(100))

plt.scatter(x,y, c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()