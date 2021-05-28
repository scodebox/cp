# Given an n x n matrix mat[n][n] of integers,
# find the maximum value of mat(c, d) – mat(a, b)
# over all choices of indexes such that both c > a and d > b.

import sys

# TC: O(CxR) | SC: O(CxR)


def find_max_diff(matrix):
    # max difference
    max_value = -sys.maxsize-1

    # print(max_value)

    # temp matrix just copied the item of last row last column value
    temp_m = [[0 for x in matrix[0]]
              for y in matrix]
    temp_m[-1][-1] = matrix[-1][-1]

    # initilize the last row and col

    for i in range(len(temp_m)-2, -1, -1):
        # initilize the last col
        if matrix[i][-1] > temp_m[i+1][-1]:
            temp_m[i][-1] = matrix[i][-1]
        else:
            temp_m[i][-1] = temp_m[i+1][-1]

    for i in range(len(temp_m[0])-2, -1, -1):
        # initilize the last row
        if matrix[-1][i] > temp_m[-1][i+1]:
            temp_m[-1][i] = matrix[-1][i]
        else:
            temp_m[-1][i] = temp_m[-1][i+1]

    # computer remaining matrix
    for i in range(len(matrix)-2, -1, -1):
        for j in range(len(matrix[0])-2, -1, -1):
            # update the max_value
            if (temp_m[i+1][j+1]-matrix[i][j]) > max_value:
                max_value = temp_m[i+1][j+1]-matrix[i][j]

            # update temp matrix
            temp_m[i][j] = max(matrix[i][j], max(
                temp_m[i][j+1], temp_m[i+1][j]))

    return max_value


if __name__ == '__main__':
    # 18
    matrix1 = [[1, 2, -1, -4, -20],
               [-8, -3, 4, 2, 1],
               [3, 8, 6, 1, 3],
               [-4, -1, 1, 7, -6],
               [0, -4, 10, -5, 1]]

    # 8
    matrix2 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

    print(find_max_diff(matrix1))
    print(find_max_diff(matrix2))
