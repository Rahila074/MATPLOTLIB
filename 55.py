#legend
#to add a list of explanation for each wedge,use the legend() function:
#add a legend ?

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["apples","cherries","bananas","date"]

plt.pie(y,labels = mylabels)
plt.legend()
plt.show()