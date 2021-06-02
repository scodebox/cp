
# TC: O(R+C) | SC: O(1)


def search(mat, key):
    # starting at -> first row last col
    col = len(mat)-1
    row = 0

    while col >= 0 and row < len(mat):
        # match
        if mat[row][col] == key:
            return(row, col)

        # previous col if key is smaller
        elif mat[row][col] > key:
            col -= 1
        # next row id key is bigger
        elif mat[row][col] < key:
            row += 1

    return (-1, -1)


if __name__ == '__main__':
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]

    print(search(mat, 29))
    print(search(mat, 100))
