#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul.

This module provides a function to perform matrix multiplication using
NumPy's `matmul` function. The matrices are first converted into NumPy arrays,
and then the multiplication is computed.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's `matmul` function.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.
    """
    arr_a = np.array(m_a)

    arr_b = np.array(m_b)

    m_result = np.matmul(arr_a, arr_b)

    return m_result
