#multiple line
#plt.plot() functions

#draw two lines by specifying a plt.plot()
#function for each line:

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3,8,1,10])
y2 =np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)
plt.show()