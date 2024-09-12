#!/usr/bin/python3


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    m_result = np.matmul(arr_a, arr_b)

    return m_result
