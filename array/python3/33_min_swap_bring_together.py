# TC: O(n) | SC: O(1)
# Sliding window technique.


def solution_1(arr, k):
    # counter total elements <=k.
    total_elements = 0
    for element in arr:
        if element <= k:
            total_elements += 1

    # total number of swap required inside the startng phase of window.
    windows_end = total_elements-1
    global_swap = 0
    for i in range(0, windows_end+1):
        if arr[i] > k:
            global_swap += 1

    # sliding window & and count swap.
    local_swap = global_swap
    windows_start = 0
    windows_end += 1
    while (windows_end < len(arr)):
        if arr[windows_end] > k:
            local_swap += 1
        if arr[windows_start] > k:
            local_swap -= 1
        windows_start += 1

        windows_end += 1
        global_swap = min(global_swap, local_swap)

    return global_swap


if __name__ == '__main__':
    arr = [2, 1, 5, 6, 3]
    k = 3

    # arr = [2, 7, 9, 5, 8, 7, 4]
    # k = 5

    # arr = [1, 12, 10, 3, 14, 10, 5]
    # k = 8

    # arr = [1, 5, 4, 7, 2, 10]
    # k = 6
    print('solution_1: ', solution_1(arr, k))
