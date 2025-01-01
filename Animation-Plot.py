import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def fun_update(frame):
    line1.set_data(x[:frame+1], y1[:frame+1])
    line2.set_data(x[:frame+1], y2[:frame+1])
    return line1, line2

frames = 100
x = np.linspace(0, 2, frames)
y1 = np.sin(x * np.pi)
y2 = np.cos(x * np.pi)

fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (6,4), sharex = True)

line1, = axes[0].plot([], [], label=r'$Sin(\phi)$', color='blue')
line2, = axes[1].plot([], [], label=r'$Cos(\phi)$', color='red')

for ax in axes:
    ax.set_xlim(0, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.legend()
    ax.grid()

axes[0].set_title("Trigonometric functions Plots")
axes[0].set_ylabel(r'$Sin(\phi)$')
axes[1].set_ylabel(r'$Cos(\phi)$')
axes[1].set_xlabel(r'$\phi (\pi)$')

fig.tight_layout()

ani = FuncAnimation(fig, func=fun_update, frames=frames, interval=30)
plt.show()