# Animation plot with FuncAnimation() of Matplotlib

# Animated Plot for Sine and Cosine  

This repository contains a Python script that creates an animated visualization of the sine and cosine functions using the `matplotlib` and `numpy` libraries.  

## Overview  

The script generates a plot showing the sine and cosine functions over the range of 0 to 2 (in terms of multiples of π). The animation reveals how these two functions evolve over time, providing a visual understanding of their behavior.  

## Requirements  

To run the script, make sure you have Python installed and the following libraries:  

- `import numpy as np`
- `import matplotlib.pyplot as plt`
- `from matplotlib.animation import FuncAnimation`

## 1. Simple Animation Plot in Python
- First, configure a plot area:
```
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6, 4), sharex=True)
```
- Then, initialize empty plots (with no data yet) for sine and cosine functions:
```
line1, = axes[0].plot([], [], label=r'$Sin(\phi)$', color='blue')  
line2, = axes[1].plot([], [], label=r'$Cos(\phi)$', color='red')
```
- After that, initialize the plot details.
```
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
```
- Finally, create the animation and display it:
```
ani = FuncAnimation(fig, func=fun_update, frames=frames, interval=30)
plt.show()
```
## 2. Showing Animation Plot in Jupyter Notebook
To display animations in a Jupyter Notebook, you need to add the following steps:
- Add this library.
```
from IPython.display import HTML 
```
- Change the end of the code to show the animation plot correctly:
```
ani = FuncAnimation(fig, func=fun_update, frames=frames, interval=30)
# HTML(ani.to_jshtml()) # Or
display(HTML(ani.to_jshtml()))
plt.close() # To close the extra plot figure
```
## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen) ![License](https://img.shields.io/badge/License-MIT-blue)
