#matplotlib pie chart
#creating pie chart s
#with pyplot ,you can use the pie() function to draw pie charts:

#A simple pie chart :

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])

plt.pie(y)
plt.show()