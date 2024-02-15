#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    m_a (list): The first matrix as a list of lists of integers or floats.
    m_b (list): The second matrix as a list of lists of integers or floats.

    Raises: ValueError:
    If the matrices cannot be multiplied due to incompatible dimensions.

    Returns:
    numpy.ndarray: The result of multiplying the two matrices.
    """
    result = np.matmul(m_a, m_b)
    return result
