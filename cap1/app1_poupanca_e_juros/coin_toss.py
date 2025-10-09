# %%
import sys
import os
import numpy as np


def coin(up_prob=0.5):
    """
    Simulates a biased coin toss.

    Args:
        up_prob (float, optional): Probability of getting "up" (result = 1).
            Must be between 0 and 1. Default is 0.5 (fair coin).

    Returns:
        int: 1 if the coin shows "up", 0 if it shows "down".
    """
    import random as rd

    up_or_down = [0, 1]

    probabilities = [1-up_prob, up_prob]

    decision = rd.choices(up_or_down, weights=probabilities)[0]
    return decision

def geometric_random_walk(initial_value=100, up_prob=0.5, steps=1000):
    """
    Generates a Geometric Random Walk trajectory.

    At each step, the value is multiplied by 1.01 (if up)
    or by 0.99 (if down).

    Args:
        initial_value (float, optional): Starting value of the process. Default = 100.
        up_prob (float, optional): Probability of going up at each step. Default = 0.5.
        steps (int, optional): Number of steps in the simulation. Default = 1000.

    Returns:
        numpy.ndarray: 1D array with the time evolution of the process.
    """
    y = np.zeros(steps)
    y[0] = initial_value

    for i in range(1, len(y)):
        if coin(up_prob=up_prob) == 1:
            y[i] = y[i-1] * 1.01
        else:
            y[i] = y[i-1] * 0.99
    return y

def arithmetric_random_walk(initial_value=100, up_prob=0.5, steps=1000):
    """
    Generates an Arithmetic Random Walk trajectory.

    At each step, the value is incremented by +1 (if up)
    or decremented by -1 (if down).

    Args:
        initial_value (float, optional): Starting value of the process. Default = 100.
        up_prob (float, optional): Probability of going up at each step. Default = 0.5.
        steps (int, optional): Number of steps in the simulation. Default = 1000.

    Returns:
        numpy.ndarray: 1D array with the time evolution of the process.
    """
    y = np.zeros(steps)
    y[0] = initial_value

    for i in range(1, len(y)):
        if coin(up_prob=up_prob) == 1:
            y[i] = y[i-1] + 1
        else:
            y[i] = y[i-1] - 1
    return y
# %%
if __name__ == "__main__":
    for i in range(10):
        print(coin(0.4))
    print(geometric_random_walk())
    print(arithmetric_random_walk())

# %%
