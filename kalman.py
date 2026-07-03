import numpy as np


def kalman_filter(
    measurements,
    A,
    H,
    Q,
    R,
    x0,
    P0,
):
    x = x0.copy()
    P = P0.copy()

    I = np.eye(x.shape[0])

    estimated_positions = []
    estimated_velocities = []

    for z in measurements:

        # Prediction
        x_pred = A @ x
        P_pred = A @ P @ A.T + Q

        # Innovation
        y = np.array([[z]]) - H @ x_pred

        S = H @ P_pred @ H.T + R

        K = P_pred @ H.T @ np.linalg.inv(S)

        # Correction
        x = x_pred + K @ y

        # Old line: P = (I - K @ H) @ P_pred
        # New Joseph Form:
        I_KH = I - K @ H
        P = I_KH @ P_pred @ I_KH.T + K @ R @ K.T

        estimated_positions.append(x[0, 0])
        estimated_velocities.append(x[1, 0])

    return estimated_positions, estimated_velocities