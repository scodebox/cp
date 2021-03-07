# TC: O(m*n) | SC: O(1)
def solution_1(m):
    # direction
    dir = 0

    # bound
    top = 0
    down = len(m)-1
    left = 0
    right = len(m[0])-1

    # traversal
    while top <= down and left <= right:
        # right
        if 0 == dir:
            for i in range(left, right+1):
                print(m[top][i], end=' ')
            top += 1
        # down
        elif 1 == dir:
            for i in range(top, down+1):
                print(m[i][right], end=' ')
            right -= 1
        # left
        elif 2 == dir:
            for i in range(right, left-1, -1):
                print(m[down][i], end=' ')
            down -= 1
        # up
        elif 3 == dir:
            for i in range(down, top-1, -1):
                print(m[i][left], end=' ')
            left += 1
        dir = (dir+1) % 4

    print()


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # m = [[1, 2,   3,  4, 5,  6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

    solution_1(m)
