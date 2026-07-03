import numpy as np
import matplotlib.pyplot as plt


def plot_results(
    true_positions,
    measurements,
    estimated_positions,
):
    plt.figure(figsize=(12, 6))

    plt.plot(
        true_positions,
        linewidth=2,
        label="True Position"
    )

    plt.scatter(
        range(len(measurements)),
        measurements,
        color="red",
        alpha=0.5,
        s=20,
        label="Measurements"
    )

    plt.plot(
        estimated_positions,
        linewidth=2,
        color="green",
        label="Kalman Estimate"
    )

    plt.xlabel("Time Step")
    plt.ylabel("Position")

    plt.grid(True)
    plt.legend()

    plt.show()


def calculate_rmse(true_values, estimated_values):
    true_values = np.array(true_values)
    estimated_values = np.array(estimated_values)

    return np.sqrt(
        np.mean((true_values - estimated_values) ** 2)
    )