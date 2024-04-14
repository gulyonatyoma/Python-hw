import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)
R = X ** 2 + Y ** 2
Z = np.sin(R) / R

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surface = ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.viridis)
ax.set_zlim(-0.4, 1)

fig.colorbar(surface)

plt.show()