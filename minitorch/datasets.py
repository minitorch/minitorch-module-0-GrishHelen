import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    """
    Generate N random 2D points uniformly distributed in [0, 1]x[0, 1].
    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    """
    Create a simple vertical split dataset
    with a clear vertical decision boundary at x1 = 0.5.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    """
    Create a diagonal split dataset
    with a linear diagonal decision boundary.

    Points are classified based on whether x1 + x2 < 0.5.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    """
    Create a dataset with two vertical splits.

    Points are classified as 0 if 0.2 < x1 < 0.8, otherwise 1.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    """
    Create an XOR-like dataset.

    The plane is divided as a 2x2 square.
    Points of class 1 are located in upper left and lower right corners.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):
    """
    Create a circular dataset.

    Class 1: outside the circle, Class 0: inside the circle.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    """
    Create a spiral dataset with two interleaved spirals.
    """

    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0

    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5,
          y(10.0 * (float(i) / (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    X = X + [(y(-10.0 * (float(i) / (N // 2))) + 0.5,
              x(-10.0 * (float(i) / (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {'Simple': simple, 'Diag': diag, 'Split': split, 'Xor': xor,
            'Circle': circle, 'Spiral': spiral}
