# Kalman Filter from Scratch

## Overview

This project implements a linear Kalman Filter using NumPy only.

The objective is to estimate an object's position and velocity
from noisy position measurements.

## State Vector

x = [position, velocity]^T

## Motion Model

x_k = A x_(k-1) + w

where

A = [[1, dt],
     [0, 1]]

## Measurement Model

z = Hx + v

H = [1 0]

## Covariance

Q : Process Noise

R : Measurement Noise

The use of the Joseph Form covariance update for numerical robustness and the coupled process noise matrix ($Q$) derived from continuous acceleration perturbations makes this approach more refined.

## Root Mean Square Error (RMSE)
Measurement : 2.030
Kalman      : 1.150
