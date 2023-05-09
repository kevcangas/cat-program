from utils.bezier import Bezier
import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt

#~~~#

fig = plt.figure(dpi=128)

#~~~# Simple arch.

t_points = np.arange(0, 1, 0.01)
test = a([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]])
curve1 = Bezier.Curve(t_points, test)

plt.plot(
	curve1[:, 0],   # x-coordinates.
	curve1[:, 1]    # y-coordinates.
)

plt.xlim([-180,180])
plt.ylim([-200,0])

plt.show()
