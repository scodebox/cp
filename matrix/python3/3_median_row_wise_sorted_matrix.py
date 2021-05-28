from bisect import bisect_right as binary_search


# TC: O(m log(m*n)) | SC: O(1)
def solution_1(m):
    # get the min and max value from matrix
    max_item = m[0][0]
    min_item = m[0][-1]
    for row in m:
        if min_item > row[0]:
            min_item = row[0]
        if max_item < row[-1]:
            max_item = row[-1]

    # calulate the median position in sorted [min to max]
    median_pos = ((len(m[0])*len(m))+1)//2

    # Binary search b/w min - max and checking the number of item less than equal to each item.
    while min_item < max_item:
        # to count number of item less than equalto mid.
        counter = 0
        mid = (min_item+max_item)//2

        for row in m:
            counter += binary_search(row, mid)
        if counter < median_pos:
            min_item = mid+1
        else:
            max_item = mid

    return min_item


if __name__ == '__main__':
    m = [[1, 3, 4], [2, 5, 6], [7, 8, 9]]
    # m = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    # m = [[1], [2], [3]]

    print('solution_1: ', solution_1(m))
