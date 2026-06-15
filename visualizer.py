from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


def plot_curves(ax, n, d, data_points, uniform_curve, uniform_pts, chordal_curve, chordal_pts):
    """Plots raw data alongside uniform and chordal fitted Bezier curves."""
    r_color, f1_color, f2_color = 'orange', 'aqua', 'm'
    ax.set_facecolor('k')

    # Data Points
    ax.scatter(data_points[:, 0], data_points[:, 1], label="Data Points", alpha=0.6, color=r_color, zorder=4)
    ax.plot(data_points[:, 0], data_points[:, 1], linestyle="--", alpha=0.2, color=r_color, zorder=3)

    # Uniform Fitting
    ax.plot(uniform_curve[:, 0], uniform_curve[:, 1], label="Uniform", color=f1_color)
    ax.scatter(uniform_pts[:, 0], uniform_pts[:, 1], label="Uniform Fits", alpha=0.6, color=f1_color, zorder=3)

    # Chordal Fitting
    ax.plot(chordal_curve[:, 0], chordal_curve[:, 1], label="Chordal", color=f2_color)
    ax.scatter(chordal_pts[:, 0], chordal_pts[:, 1], label="Chordal Fits", alpha=0.6, color=f2_color, zorder=3)

    ax.set_title(f"{n} Data Points, \n {d} Control Points")
    ax.legend(fontsize='small')


def plot_error_matrix(ax, error_uniform, error_chordal):
    # todo: mean error is more insightful

    # CREATE COLORMAP
    import matplotlib.colors as mcolors
    colors = [(1, 1, 1), (1, 0, 0)]
    w2r = mcolors.LinearSegmentedColormap.from_list("w2r", colors, N=256)

    # PLOT MATRIX
    error_matrix = np.stack([error_uniform, error_chordal], axis=0)
    im = ax.imshow(error_matrix, cmap=w2r, vmin=0)

    # LABEL CELLS
    for i in range(error_matrix.shape[0]):
        for j in range(error_matrix.shape[1]):
            cell_val = error_matrix[i, j]
            text_color = 'k' if cell_val <= (error_matrix.max() / 2) else 'w'
            ax.text(j, i, f"{cell_val:.3f}", ha="center", va="center", color=text_color)

    # LABEL AXES
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['X', 'Y'])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Uniform', 'Chordal'])

    ax.set_title("Average Error")


def plot_a_matrix(ax, A):
    """Plots the system Matrix A with cell value overlays."""
    im = ax.imshow(A, cmap="cubehelix")

    for i, line in enumerate(A):
        for j, cell in enumerate(line):
            text_color = 'w' if cell <= 0.5 else 'k'
            ax.text(j, i, f"{cell:.2f}", ha="center", va="center", color=text_color)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Matrix A")


def experiment_show(
        n, d,
        data_points,

        fitted_bezier_uniform,
        fitted_data_points_uniform,
        error_uniform,

        fitted_bezier_chordal,
        fitted_data_points_chordal,
        error_chordal,
):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    plot_curves(
        axes[0], n, d, data_points,
        fitted_bezier_uniform, fitted_data_points_uniform,
        fitted_bezier_chordal, fitted_data_points_chordal
    )

    plot_error_matrix(
        axes[1],
        error_uniform,
        error_chordal
    )

    plt.tight_layout()

    # Save step
    path = "output/Experiment.svg"
    Path("output").mkdir(parents=True, exist_ok=True)
    plt.savefig(path)
    plt.close(fig)