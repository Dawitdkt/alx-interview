#!/usr/bin/python3

def rotate_matrix(mat):
    n = len(mat)  # assuming the matrix is square
    """_summary_
  """
    for i in range(n // 2):  # iterate over each square cycle
        for j in range(i, n - i - 1):  # iterate over each element in the cycle
            # swap elements of each cycle in clockwise direction
            temp = mat[i][j]
            mat[i][j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = temp
