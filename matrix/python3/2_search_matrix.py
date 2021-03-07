# TC: O(max(m,n)) | SC: O(1)
def solution_1(m, target):
    x = 0
    y = len(m[0])-1

    while x <= len(m)-1 and y >= 0:
        if m[x][y] == target:
            return True
        elif m[x][y] < target:
            # move down
            x += 1
        elif m[x][y] > target:
            # move left
            y -= 1

    return False


# TC: O(log(m*n)) | SC: O(1)

# Map from sequence to matrix index:
# row = sequence no / row_len
# col = sequence no % row_len
# m[sequence no / row_len][sequence no % row_len]

def solution_2(m, target):
    row_len = len(m[0])
    low = 0
    high = (len(m)*row_len)-1

    # binary search for the value.
    while low <= high:
        mid = (low+high)//2

        # mapping from sequence number to 2D array index.s
        if m[mid//row_len][mid % row_len] == target:
            return True
        elif m[mid//row_len][mid % row_len] < target:
            low = mid+1
        else:
            high = mid-1

    return False


if __name__ == '__main__':
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 11

    # m = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]]
    # target = 2

    print('solution_1: ', solution_1(m, target))
    print('solution_2: ', solution_2(m, target))
