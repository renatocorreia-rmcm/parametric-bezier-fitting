from pathlib import Path

import numpy as np
from random import randrange

from matplotlib import pyplot as plt

import bezier
from parameterize import parameterize
from visualizer import experiment_show

"""
    EXPERIMENT PARAMETERS
"""

n = 4  # amount of data points
d = 3  # amount of control points (Bézier curve Degree). If d<n, get best solution by LSM

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
samples = np.linspace(0, 1, 8 * n)  # 8 samples per segment

raw_bezier = np.array([bezier.interpolate(data_points, t) for t in samples])  # data points as control points
fitted_bezier_uniform = np.array(
    [bezier.interpolate(control_points_uniform, t) for t in samples])  # fitted control points uniform
fitted_bezier_chordal = np.array(
    [bezier.interpolate(control_points_chordal, t) for t in samples])  # fitted control points chordal

"""
    PLOTTING
"""

experiment_show(
    data_points,
    fitted_bezier_uniform,
    error_uniform,
    fitted_bezier_chordal,
    error_chordal
)
