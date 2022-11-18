
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


# Multiple points
ax=plt.axes(projection="3d")
#x_data = np.random.randint(0,100,(500,))
#y_data = np.random.randint(0,100,(500,))
#z_data = np.random.randint(0,100,(500,))


#x_data=np.arange(-5,5,0.1)
#y_data=np.arange(-5,5,0.1)
from DataInput import xValuesDouble
x_data=xValuesDouble




X,Y=np.meshgrid(x_data,y_data)
Z=np.sin(X)*np.cos(Y)
ax.plot_surface(X,Y,Z, cmap="RdYlGn")
plt.show()

