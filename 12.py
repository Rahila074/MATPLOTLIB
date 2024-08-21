# use both MEC and MFC
#arguments to color the entire marker:

#set the color of both the edge and the face red?

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,6,1,10])

plt.plot(ypoints,marker='o',ms = 20, mec = 'r',mfc = 'r')
plt.show()