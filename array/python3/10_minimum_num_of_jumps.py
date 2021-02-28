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


# Dynamic programming
# TC: O(n^2)
# SC: O(n)
def solution_2(arr):
    # Invalid input
    if len(arr) <= 1 or 0 == arr[0]:
        return None

    # To store min step to reach each elements.
    min_step = [0]*len(arr)

    for i in range(1, len(arr)):
        # Calculating min step to reach element arr[i].
        for j in range(0, i):
            if j+arr[j] >= i:
                min_step[i] = min_step[j]+1
                break

        # If arr[i] element is not reachable. so last element is not also reachable.
        if 0 == min_step[i]:
            return None

    return (min_step[len(arr)-1])


# Dynamic programming
# TC: O(n)
# SC: O(1)
def solution_3(arr):
    # Invalid input
    if len(arr) <= 1 or 0 == arr[0]:
        return None

    # to store maximum reachable index of the array.
    max_reachable_index = arr[0]
    # each step of a jump.
    step = arr[0]
    # tract number of jumps to reach end.
    jump = 1
    # # index of the array.
    # index = 1

    # Traversing the array.
    for index in range(1, len(arr)):
        # reached to the end return the jumps.
        if index == len(arr)-1:
            return jump
        # decreasing the step by 1.| take a new step.
        step -= 1
        # updating the maximum reachable index with new step.
        if max_reachable_index < (index + arr[index]):
            max_reachable_index = index + arr[index]

        # when step is 0 count it as a jump.
        if 0 == step:
            jump += 1
            # The end is not rechable condition.
            if index >= max_reachable_index:
                return None
            step = arr[index]


if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]  # 3
    # arr = [1, 3, 0, 0, 0, 0, 6, 7, 6, 8, 9]  # Not reachable None
    # arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 10
    # arr = [0, 0, 0, 0]  # Not rechable None
    # arr = [1, 1, 1, 1]  # 3

    print("solution_1 : {}".format(solution_1(arr)))
    print("solution_2 : {}".format(solution_2(arr)))
    print("solution_3 : {}".format(solution_3(arr)))