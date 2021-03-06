# Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).


# TC: O(n) | SC: O(1)
def solution_1(arr, value):

    # if single element greater than value
    for item in arr:
        if item > value:
            return 1

    start = 0
    end = 0
    sum = 0
    min_len = len(arr)

    # keep adding while sum is < value.
    while end < len(arr) and sum <= value:
        sum += arr[end]
        end += 1

    # Check smaller sub array is available or not.
    while start < len(arr) and sum > value:
        # update len and remove starting item.
        if (end-start) < min_len:
            min_len = end-start
        sum -= arr[start]
        start += 1

    return min_len


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 0, 19]
    value = 51

    # arr = [1, 10, 5, 2, 7]
    # value = 9

    # arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    # value = 280

    # arr = [1, 2, 3, 4, 1, 2, 10]
    # value = 5

    print('solution_1: ', solution_1(arr, value))
