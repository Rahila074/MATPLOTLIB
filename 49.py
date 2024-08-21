#matplotlib histogram
#histogram
#A histogram  is a graph showing freqency distributions.
#it is a graph showing the number of observation within each given interval
#the hist() function will read the array and produce a histogram:

#A simple histogram
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()