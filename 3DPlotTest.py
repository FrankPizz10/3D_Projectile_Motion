import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


# References
# https://gist.github.com/neale/e32b1f16a43bfdc0608f45a504df5a84
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# https://riptutorial.com/matplotlib/example/23558/basic-animation-with-funcanimation

# ANIMATION FUNCTION
def func(num, dataSet, line, redDots):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])
    line.set_3d_properties(dataSet[2, :num])
    redDots.set_data(dataSet[0:2, :num])
    redDots.set_3d_properties(dataSet[2, :num])
    return line


# THE DATA POINTS
g = -9.8
V = 45
degrees = 45
alpha = degrees * 0.017453
p = 1.23  # air density
A = 0.00426  # Surface area of a baseball
C = .4  # drag coefficient
m = 0.145  # mass of a baseball in kg


t = np.arange(0, 8, .2)  # This would be the z-axis ('t' means time here)
# x = np.cos(t) - 1
# y = 1 / 2 * (np.cos(2 * t) - 1)
# x = X0 + (V0X*t) + (.5*g*(t*t))
# y = Y0 + (V0Y*t) + (.5*g*(t*t))
Vx = V * np.cos(alpha)
Vy = V * np.sin(alpha)

Vt = m*g*C

dragA = -((p*A*C*(Vx*Vx))/(2*m))
# x = (Vx * t) + (.5*dragA*(t*t))
x = Vx * t
y = (Vy * t) + (.5*g*(t*t))
z = np.zeros(40)

dataSet = np.array([x, z, y])
numDataPoints = len(t)

# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='r', marker='o')[0]  # For scatter plot
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0]  # For line plot

# AXES PROPERTIES]
ax.set_xlim(0, max(dataSet[0]))
ax.set_zlim(0, max(dataSet[2]))
# ax.set_xlim3d([limit0, limit1])
ax.set_xlabel('X(t)')
ax.set_ylabel('Z(t)')
ax.set_zlabel('Y(t)')
ax.set_title('HuskyCast')

# Creating the Animation object
# line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet, line, redDots), interval=50,
#                                    blit=False)
# line_ani.save(r'Animation.mp4')

# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# ax.set_xlim(0, max(dataSet[0]))
# ax.set_zlim(0, max(dataSet[2]))
#
# # Data for a three-dimensional line
#
# ax.plot3D(dataSet[0], dataSet[1], dataSet[2], 'blue')

plt.show()
