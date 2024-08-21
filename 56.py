#legend with header
# to add a header to the legend,
#add the title parameter to the legend function.
#add a legend with a header ?

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["apples","cherries","bananas","date"]

plt.pie(y,labels = mylabels)
plt.legend(title = "for fruites:")
plt.show()