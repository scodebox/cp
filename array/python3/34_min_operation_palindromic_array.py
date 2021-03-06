# TC: O(n) | SC: O(n)
def solution_1(arr):
    start = 0
    end = len(arr)-1
    operation = 0

    while start < end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
        # Merge smaller elements.
        elif arr[start] < arr[end]:
            start += 1
            arr[start] = arr[start]+arr[start-1]
            operation += 1
        else:
            end -= 1
            arr[end] = arr[end]+arr[end+1]
            operation += 1

    return operation


if __name__ == '__main__':
    arr = [1, 4, 5, 1]  # 1
    # arr = [15, 4, 15]  # 0
    # arr = [11, 14, 15, 99]  # 3
    # arr = [1, 7, 9, 1]  # 1
    # arr = [1, 3, 8, 6, 1]  # 2
    # arr = [1, 2, 3, 5, 3, 2, 4]  # 4

    print('solution_1: ', solution_1(arr))
