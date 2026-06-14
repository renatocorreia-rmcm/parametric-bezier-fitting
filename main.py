import numpy as np
from random import randrange

from matplotlib import pyplot as plt

import bezier
from parameterize import parameterize

"""
    EXPERIMENT PARAMETERS
"""

n = 4  # amount of data points
d = 2  # amount of control points (Bézier curve Degree). If d<n, get best solution by LSM

rb = 10  # Bounds for random data points

"""
    DATA POINTS
"""

data_points = np.array(
    [[randrange(-rb, rb), randrange(-rb, rb)] for i in range(n)]
)

"""
    AUTO-PARAMETERIZATION
"""

parameters_uniform = parameterize(data_points, 0)
parameters_chordal = parameterize(data_points, 1)

"""
    BEZIER FITTING
"""

# find control points
control_points_uniform = bezier.fit(data_points, parameters_uniform, d)
control_points_chordal = bezier.fit(data_points, parameters_chordal, d)

# sample polynomial
samples = np.linspace(0, 1, 8 * n)  # 8 samples per segment

raw_bezier = np.array([bezier.interpolate(data_points, t) for t in samples])  # data points as control points
fitted_bezier_uniform = np.array(
    [bezier.interpolate(control_points_uniform, t) for t in samples])  # fitted control points uniform
fitted_bezier_chordal = np.array(
    [bezier.interpolate(control_points_chordal, t) for t in samples])  # fitted control points chordal

"""
    PLOTTING
"""

r_color = 'orange'  # raw curve color
f1_color = 'aqua'  # fitted curve 1 color
f2_color = 'm'  # fitted curve 2 color

plt.gca().set_facecolor('k')


# RAW DATA POINTS POLYGON
plt.scatter(data_points[:, 0], data_points[:, 1], label="Data Points", alpha=0.6, color=r_color)
plt.plot(data_points[:, 0], data_points[:, 1], linestyle="--", alpha=0.2, color=r_color)

# RAW BEZIER CURVE
# plt.plot(raw_bezier[:, 0], raw_bezier[:, 1], label="Raw Bezier Curve", color=r_color)


# UNIFORM PARAMETERIZATION

# fitted control points polygon
# plt.scatter(control_points_uniform[:,0],control_points_uniform[:,1],
#             label="Control Points", alpha=0.2, color=f1_color)
# plt.plot(control_points_uniform[:,0],control_points_uniform[:,1],
#          linestyle="--", alpha=0.1, color=f1_color)

# fitted bezier curve
plt.plot(fitted_bezier_uniform[:, 0], fitted_bezier_uniform[:, 1],
         label="Uniform", color=f1_color)

# CHORDAL PARAMETERIZATION

# fitted control points polygon
# plt.scatter(control_points_chordal[:, 0], control_points_chordal[:, 1],
#             label="Control Points", alpha=0.2, color=f2_color)
# plt.plot(control_points_chordal[:, 0], control_points_chordal[:, 1],
#          linestyle="--", alpha=0.1, color=f2_color)

# fitted bezier curve
plt.plot(fitted_bezier_chordal[:, 0], fitted_bezier_chordal[:, 1],
         label="Chordal", color=f2_color)

# PLOTTING

plt.title("Fitted Bézier Curves")
plt.legend()
plt.show()
