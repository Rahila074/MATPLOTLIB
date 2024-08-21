#create a title for a plot
#you can use the title () function to set a title for the plot
#add a plot title and labels for the x-and y-axis ?

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("Sports watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burnage ")
plt.show()