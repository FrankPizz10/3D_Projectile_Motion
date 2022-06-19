import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import numpy as np


def y_location(x, vel_horizontal, vel_vertical, acceleration):
    """
    Get the veritical location of the ball

    x = v1 * t
    y = v2 * t + (a * t^2) / 2

    After subsituting t = x / v1 in f(y) => y = v2 * (x / v1) + (a * x^2) / (2 * v1^2)
    """
    b = vel_horizontal / vel_vertical
    a = acceleration / (2 * vel_vertical**2)

    return a * x**2 + b * x


parser = ArgumentParser(description="Ball trajectory finder", formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("--x-starts", type=float, help="positive start range of x axis", default=-10, metavar="X START")
parser.add_argument("--x-ends", type=float, help="positive end range of x axis", default=10, metavar="X END")
parser.add_argument("--total-points", type=int, help="number of points to generate between start of x and end of x", default=500, metavar="POINTS")
parser.add_argument("--v1", type=float, help="initial horizontal velocity", metavar="VELOCITY", required=True)
parser.add_argument("--v2", type=float, help="initial vertical velocity", metavar="VELOCITY", required=True)
parser.add_argument("--acc", type=float, help="acceleration of the ball towards the ground", metavar="ACCELERATION", default=-9.81)

args = parser.parse_args()

x_arr = np.linspace(args.x_starts, args.x_ends, args.total_points)
y_arr = np.array([y_location(x, args.v1, args.v2, args.acc) for x in x_arr])  # getting y location from x

plt.plot(x_arr, y_arr)
plt.xlabel("Horizontal distance")
plt.ylabel("Vertical distance")
plt.title("Ball trajectory")
plt.savefig("plot.png")
plt.show()
