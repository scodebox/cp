import sys

# Brute Force & Top Down approach
# TC: O(n^n)
# SC: O(1)


def solution_1(arr, index=0):
    #  exit condition.
    if len(arr)-1 == index:
        return 0

    min_step = sys.maxsize

    # Try the all possible steps.
    for step in range(1, arr[index]+1):
        if index+step < len(arr):
            temp_step = solution_1(arr, index+step)
            if None == temp_step:
                continue
            # Take th minimum one.
            min_step = min(min_step, temp_step)
            # print(index+step, arr[index+step], temp_step)

    # If array element was zero | arr[index]==0.
    if sys.maxsize == min_step:
        return None
    # return min + 1.
    return (min_step+1)


if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]  # 3
    # arr = [1, 3, 0, 0, 0, 0, 6, 7, 6, 8, 9]  # Not reachable -1
    # arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 10
    # arr = [0, 0, 0, 0]  # Not rechable -1
    # arr = [1, 1, 1, 1]  # 3

    print("solution_1 : {}".format(solution_1(arr)))
