# TC: O(n) | SC: O(1)
def solution_1(arr, low_val, high_val):
    start = 0
    end = len(arr)-1
    index = 0

    while index < end:
        if arr[index] < low_val:
            arr[index], arr[start] = arr[start], arr[index]
            start += 1
        elif arr[index] > high_val:
            arr[index], arr[end] = arr[end], arr[index]
            end -= 1
            index -= 1
        index += 1

    return arr


if __name__ == '__main__':
    arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    low_val = 14
    high_val = 20

    # low_val = 20
    # high_val = 20

    # low_val = 10
    # high_val = 20

    print('solution_1: ', solution_1(arr, low_val, high_val))
