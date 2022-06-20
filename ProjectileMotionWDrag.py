import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import math

g = 9.8
p = 1.23
A = 0.00426
C = .4
m = 0.145
degrees = 30
alpha = degrees * 0.017453

V = 25

Vx = V * np.cos(alpha)
Vy = V * np.sin(alpha)

D = (p * C * A)/2

Ax = -(D/m)*V*Vx
Ay = -(g) - (D/m)*V*Vy

dT = 0.05

size = 45

VxArr = np.zeros(size)
VyArr = np.zeros(size)
XPosArr = np.zeros(size)
YPosArr = np.zeros(size)
AxArr = np.zeros(size)
AyArr = np.zeros(size)

VxArr[0] = Vx
VyArr[0] = Vy
XPosArr[0] = 0
YPosArr[0] = 0
AxArr[0] = Ax
AyArr[0] = Ay


def calcTrajectory():
    for n in range(size-1):
        VxArr[n+1] = VxArr[n] + (AxArr[n] * dT)
        VyArr[n+1] = VyArr[n] + (AyArr[n] * dT)
        V = math.sqrt((VxArr[n]**2)+(VyArr[n]**2))
        AxArr[n+1] = -(D/m)*V*Vx
        AyArr[n+1] = -(g) - (D/m)*V*Vy
        XPosArr[n+1] = XPosArr[n] + (VxArr[n]*dT) + (.5*AxArr[n]*(dT**2))
        YPosArr[n + 1] = YPosArr[n] + (VyArr[n] * dT) + (.5 * AyArr[n] * (dT ** 2))
    dataSet = np.array([XPosArr, np.zeros(size), YPosArr])


def convertToFeet():
    for i in range(len(XPosArr)):
        XPosArr[i] = XPosArr[i] * 3.28084
        YPosArr[i] = YPosArr[i] * 3.28084

calcTrajectory()
convertToFeet()

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
redDots = plt.plot(XPosArr, np.zeros(size), YPosArr, lw=2, c='r', marker='o')[0]  # For scatter plot
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(XPosArr, np.zeros(size), YPosArr, lw=2, c='g')[0]  # For line plot

# AXES PROPERTIES]
ax.set_xlim(0, max(XPosArr))
ax.set_zlim(0, max(YPosArr))
ax.set_xlabel('Distance in Feet')
ax.set_ylabel('Z(t)')
ax.set_zlabel('Height in Feet')
ax.set_title('HuskyCast')

plt.show()
