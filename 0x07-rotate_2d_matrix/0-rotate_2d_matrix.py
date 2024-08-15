#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix: list):
    """Rotate a 2D matrix by 90 degrees"""
    length = len(matrix[0])
    matrix.extend([[] for _ in range(length)])

    for i in range(len(matrix), len(matrix) - length, -1):
        for j in range(len(matrix) - length, 0, -1):
            matrix[i - 1].append(matrix[j - 1].pop())
    del matrix[0 : len(matrix) - length]
