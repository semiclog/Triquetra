import matplotlib.pyplot as plt
import numpy as np
import math

# Define radius
R = 1

# Define x offset (unit circle for 30deg is sqrt(3/2), 1/2)
offsetX = R/2
offsetY = R * np.sqrt(3) / 2
offsetY_circle =  R * np.sqrt(3) / 4

#Define linspace
line_width = 10
num = 100

# Bottom arc (0 to pi)
t1 = np.linspace(0, np.pi, num)
x1 = R * np.cos(t1)
y1 = R * np.sin(t1)

# Right arc (2/3pi to 5/3pi offset by 0.5 in x and sqrt(3)/2 in y)
t2 = np.linspace(2 * np.pi / 3, 5 * np.pi / 3, num)
x2 = R * np.cos(t2) + offsetX
y2 = R * np.sin(t2) + offsetY

# Left arc (-2/3pi to 1/3pi offset by 0.5 in x and sqrt(3)/2 in y)
t3 = np.linspace(-2 * np.pi / 3, np.pi / 3, num)
x3 = R * np.cos(t3) - offsetX
y3 = R * np.sin(t3) + offsetY

# Central circle
t4 = np.linspace(0, 2 * np.pi, num)
x4 = R/1.1 * np.cos(t4)
y4 = R/1.1 * np.sin(t4) + offsetY_circle


# Plot
plt.plot(x1, y1, 'k', linewidth=line_width, solid_capstyle='round')
plt.plot(x2, y2, 'k', linewidth=line_width, solid_capstyle='round')
plt.plot(x3, y3, 'k', linewidth=line_width, solid_capstyle='round')
plt.plot(x4, y4, 'k', linewidth=line_width, solid_capstyle='round')

plt.axis('equal')
plt.show()