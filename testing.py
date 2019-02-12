from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#set up the figure
fig = plt.figure()
ax = plt.axes(projection='3d')

#creating surface plot
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

#second plot
def f2(x, y):
    return 2**x + 0.25*y

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f2(X, Y)

ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

plt.show()
