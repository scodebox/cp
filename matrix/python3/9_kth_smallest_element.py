def counter(matrix, element):
    # count total number of element lessthan equal to element
    count = 0
    index = len(matrix[0])-1
    for row in matrix:
        # start from the right side of the row and continue as log as item is larger that element
        while index > -1:
            if row[index] <= element:
                count += index+1
                break
            index -= 1
    return count


# TC: O(N*log(N)) | SC: O(1)
def find_kth_small(matrix, k):
    # sorted matrix so apply modified binary search.
    low = matrix[0][0]
    high = matrix[-1][-1]

    while low < high:
        mid = (low+high)//2
        if counter(matrix, mid) >= k:
            high = mid
        else:
            low = mid+1

    return high


if __name__ == '__main__':
    matrix1 = [
        [16, 28, 60, 64],
        [22, 41, 63, 91],
        [27, 50, 87, 93],
        [36, 78, 87, 94]]

    matrix2 = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]

    print(find_kth_small(matrix2, 7))  # 30
    print(find_kth_small(matrix1, 3))  # 27
