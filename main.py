# todo: show resulting fitted control points
#   plot error as imshow 2x2 matrix (parameterization method) x (axis)

# todo: save A fig


import numpy as np
from random import randrange

import bezier
from parameterize import parameterize
from visualizer import experiment_show

"""
    EXPERIMENT PARAMETERS
"""

n = 5  # amount of data points
d = n-1  # amount of control points (Bézier curve Degree). If d<n, get best solution by LSM

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
control_points_uniform, error_uniform = bezier.fit(data_points, parameters_uniform, d)
control_points_chordal, error_chordal = bezier.fit(data_points, parameters_chordal, d)

# sample polynomial
samples = np.linspace(0, 1, 10 * n)  # 8 samples per segment

fitted_bezier_uniform = np.array(
    [bezier.interpolate(control_points_uniform, t) for t in samples]
)
fitted_data_points_uniform = np.array(
    [bezier.interpolate(control_points_uniform, t) for t in parameters_uniform]
)


fitted_bezier_chordal = np.array(
    [bezier.interpolate(control_points_chordal, t) for t in samples]
)
fitted_data_points_chordal = np.array(
    [bezier.interpolate(control_points_chordal, t) for t in parameters_chordal]
)


"""
    PLOTTING
"""

experiment_show(
    n, d,
    data_points,

    fitted_bezier_uniform,
    fitted_data_points_uniform,
    error_uniform,

    fitted_bezier_chordal,
    fitted_data_points_chordal,
    error_chordal,
)
