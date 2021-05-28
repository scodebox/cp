# TC: O(n^2) | SC: O(n^2)
def sol1(matrix):
    # new matrix
    rotation = [[0 for x in matrix[0]] for y in matrix]
    # make each row one col in from the end
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rotation[j][(len(matrix[0])-1)-i] = matrix[i][j]

    for row in rotation:
        print(row)


# TC: O(n^2) | SC: O(1)
def sol2(matrix):
    # transpose of matrix
    for i in range(len(matrix)):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the each row
    for i in range(len(matrix)):
        start = 0
        end = len(matrix)-1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    for row in matrix:
        print(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    sol1(matrix)
    print()
    sol2(matrix)
