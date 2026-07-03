import numpy as np

DT = 1.0
STEPS = 100

INITIAL_STATE = np.array([
    [0.0],
    [2.0]
])

A = np.array([
    [1, DT],
    [0, 1]
])

H = np.array([[1, 0]])

Q = np.array([
    [0.01, 0],
    [0, 0.01]
])

R = np.array([[4]])

INITIAL_ESTIMATE = np.array([
    [0.0],
    [0.0]
])

INITIAL_COVARIANCE = np.array([
    [1000.0, 0],
    [0, 1000.0]
])

MEASUREMENT_STD = 2