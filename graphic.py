import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)
R = X ** 2 + Y ** 2
Z = np.sin(R ** 0.5) / (R ** 0.5)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surface = ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.viridis)

fig.colorbar(surface)
ax.set_zlim(-0.2, 0.8)

plt.show()