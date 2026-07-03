import numpy as np


def simulate_motion(initial_state, A, steps):
    state = initial_state.copy()

    positions = []
    velocities = []

    for _ in range(steps):
        state = A @ state

        positions.append(state[0, 0])
        velocities.append(state[1, 0])

    return positions, velocities


def generate_measurements(true_positions, std):
    measurements = []

    for position in true_positions:
        noisy = position + np.random.normal(0, std)
        measurements.append(noisy)

    return measurements