import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1) #(1 row,2 columns. 2 nd subplot)
plt.plot(x,y)
plt.title("SALES")
#plot 2:

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)#(1 row,2 columns. 2 nd subplot)
plt.plot(x,y)
plt.title("INCOMES")
plt.suptitle("MY PLOT")
plt.show()