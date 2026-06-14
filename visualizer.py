from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def matrix_show(A):
    # label each cell
    for i, line in enumerate(A):
        for j, cell in enumerate(line):
            plt.text(
                j, i, round(cell, 3),
                ha="center", va="center", color=('w' if cell <= 0.5 else 'k')
            )

    plt.xticks([])
    plt.yticks([])
    plt.title("")
    plt.imshow(A, cmap="cubehelix")

    path = f"output/{"Matrix_1"}.svg"
    Path("output").mkdir(parents=True, exist_ok=True)
    plt.savefig(path)


def experiment_show(
    data_points,

    fitted_bezier_uniform,
    error_uniform,

    fitted_bezier_chordal,
    error_chordal,
):
    r_color = 'orange'  # raw curve color
    f1_color = 'aqua'  # fitted curve 1 color
    f2_color = 'm'  # fitted curve 2 color

    plt.gca().set_facecolor('k')

    # RAW DATA POINTS POLYGON
    plt.scatter(data_points[:, 0], data_points[:, 1], label="Data Points", alpha=0.6, color=r_color, zorder=3)
    plt.plot(data_points[:, 0], data_points[:, 1], linestyle="--", alpha=0.2, color=r_color, zorder=3)

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
             label=f"Uniform {np.round(error_uniform, 1)}", color=f1_color)

    # CHORDAL PARAMETERIZATION

    # fitted control points polygon
    # plt.scatter(control_points_chordal[:, 0], control_points_chordal[:, 1],
    #             label="Control Points", alpha=0.2, color=f2_color)
    # plt.plot(control_points_chordal[:, 0], control_points_chordal[:, 1],
    #          linestyle="--", alpha=0.1, color=f2_color)

    # fitted bezier curve
    plt.plot(fitted_bezier_chordal[:, 0], fitted_bezier_chordal[:, 1],
             label=f"Chordal {np.round(error_chordal, 1)}", color=f2_color)

    # PLOTTING

    plt.title("Fitted Bézier Curves")
    plt.tight_layout()
    plt.legend()
    path = f"output/{"Figure_1"}.svg"
    Path("output").mkdir(parents=True, exist_ok=True)
    plt.savefig(path)
