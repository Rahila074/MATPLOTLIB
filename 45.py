#color name
#you can use any of the 140 supported color names
#Draw 4 "hotpink" bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array (["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y ,color = "hotpink")
plt.show()


