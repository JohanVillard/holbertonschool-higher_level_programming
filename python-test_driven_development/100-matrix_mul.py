#!/usr/bin/python3
"""
This module contains the function 'matrix_mul.py'.

Usage:
    Enter 2 matrices (list of lists) in the function.
    For matrix multiplication, the number of columns
    in the first matrix must be equal to the number of rows
    i the second matrix. The result matrix has the number of rows
    of the first and the number of columns of the second matrix.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplie 2 matrices.

    Parameters:
        m_a (list of list): Contains integers or float.
        m_b (list of list): Contains integers or float.

    Returns:
        mul_matrix (list of lists): The function returns the result of
        the 2 matrices entered. It compute a multiplication.
    """
    # Check if parameters are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if parameters are lists of lists
    for m_list in m_a:
        if not isinstance(m_list, list):
            raise TypeError("m_a must be a list of lists")
    for m_list in m_b:
        if not isinstance(m_list, list):
            raise TypeError("m_b must be a list of lists")

    # Check if list or list of lists ar empty
    if not m_a:
        raise ValueError("m_a can't be empty")
    for m_list in m_a:
        if not m_list:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for m_list in m_b:
        if not m_list:
            raise ValueError("m_b can't be empty")

    # Check element in list of lists is integer or float
    for m_list in m_a:
        for num in m_list:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for m_list in m_b:
        for num in m_list:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check row's size
    ref_size = 0
    for m_list in m_a:
        if ref_size == 0:
            ref_size = len(m_list)
        elif ref_size != len(m_list):
            raise TypeError("each row of m_a must be of the same size")
    ref_size = 0
    for m_list in m_b:
        if ref_size == 0:
            ref_size = len(m_list)
        elif ref_size != len(m_list):
            raise TypeError("each row of m_b must be of the same size")

    # Check if the matrices can be multiplied
    if ref_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute multiplication
    total_rows = len(m_b)
    m_res = []
    for a_row in range(len(m_a)):
        # Multiplie and stores 1 row
        res_row = []
        for b_col in range(total_rows):
            sum_prod = 0
            for i in range(total_rows):
                sum_prod += m_a[a_row][i] * m_b[i][b_col]
            res_row.append(sum_prod)

        m_res.append(res_row)

    return m_res
