#color Hex
#or you can use hexadecimal color values:
#Draw 4 bars with a beautiful green color ?
import matplotlib.pyplot as plt
import numpy as np

x = np.array (["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y ,color = "#4CAF50")
plt.show()
