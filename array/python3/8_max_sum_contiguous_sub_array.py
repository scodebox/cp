import sys

# Dynamic Programming : using Kadane’s Algorithm


def max_sub_array_sum(arr):
    max_sum = -sys.maxsize-1

    for i in range(1, len(arr)):
        if arr[i] < (arr[i-1]+arr[i]):
            arr[i] = (arr[i-1]+arr[i])
        if max_sum < arr[i]:
            max_sum = arr[i]

    return max_sum


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]  # 7
    # arr=[-2, 1, -3, 4,-1, 2, 1, -5, 4] # 6
    print(max_sub_array_sum(arr))
