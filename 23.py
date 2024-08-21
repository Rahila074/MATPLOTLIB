#set font properties for title and labels
#fontdict parameter in xlable() ,ylabel(),
#and title () to set font properties for the title and labels.
#set font properties for the title and labels.


import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


font1 = {"family":'self','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data",fontdict=font1)
plt.xlabel("Average Pulse",fontdict = font2)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.plot(x,y)
plt.show()