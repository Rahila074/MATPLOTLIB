#shadow
#add a shadow to the pie chart by setting the shadows parameter to true:
#add a shadow

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels=["apples","banana","cherry","date"]
myexplode = [0.2,0,0,0]

plt.pie(y, labels = mylabels, explode=myexplode,shadow=True)
plt.show()