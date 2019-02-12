from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#set up the figure
fig = plt.figure()
ax = plt.axes(projection='3d')

#second plot
def f(x, y):
    return x+y

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_title('f(x+y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()