#line width
#linewidth or

#the shorter lw to change the width of line.

#plot with a 2.5pt wide line?

import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3,8,1,10])

plt.plot(ypoints,linewidth='20.5')
plt.show()