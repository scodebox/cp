# TC: O(m+n) | SC: O(1)
def solution_1(m):
    # last index of a row
    one_start_index = len(m[0])-1
    # track row with max 1s.
    row = -1

    # search for row with max 1s.
    for i in range(0, len(m)):
        # each row move backwards to hold starting index of 1.
        while m[i][one_start_index-1] and one_start_index > 0:
            one_start_index -= 1
            row = i

    return row


if __name__ == '__main__':
    m = [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]

    # m = [[0, 0], [1, 1]]

    # m = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]

    # m = [[0,  0, 0, 1, 1], [0, 0,  1, 1, 1], [
    #     0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 1]]

    print('solution_1: ', solution_1(m))
