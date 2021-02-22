# Kadane's Algorithm
# TC: O(n) | SC: O(1)


def kadans_algo(arr):
    global_max = arr[0]

    # Check the current value && current value + previous value >> take the max.
    for i in range(1, len(arr)):
        if arr[i] < (arr[i]+arr[i-1]):
            arr[i] = (arr[i]+arr[i-1])

        if global_max < arr[i]:
            global_max = arr[i]

    return global_max


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]  # 7
    # arr=[-2, 1, -3, 4,-1, 2, 1, -5, 4]    # 6
    print('Global max : ', kadans_algo(arr))
