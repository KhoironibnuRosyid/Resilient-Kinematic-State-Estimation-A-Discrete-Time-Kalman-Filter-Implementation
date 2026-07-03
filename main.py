from config import *

from simulation import (
    simulate_motion,
    generate_measurements,
)

from kalman import kalman_filter

from plotting import (
    plot_results,
    calculate_rmse,
)


def main():

    true_positions, true_velocities = simulate_motion(
        INITIAL_STATE,
        A,
        STEPS,
    )

    measurements = generate_measurements(
        true_positions,
        MEASUREMENT_STD,
    )

    estimated_positions, estimated_velocities = kalman_filter(
        measurements,
        A,
        H,
        Q,
        R,
        INITIAL_ESTIMATE,
        INITIAL_COVARIANCE,
    )

    plot_results(
        true_positions,
        measurements,
        estimated_positions,
    )

    measurement_rmse = calculate_rmse(
        true_positions,
        measurements,
    )

    kalman_rmse = calculate_rmse(
        true_positions,
        estimated_positions,
    )

    print(f"Measurement RMSE : {measurement_rmse:.3f}")
    print(f"Kalman RMSE      : {kalman_rmse:.3f}")


if __name__ == "__main__":
    main()