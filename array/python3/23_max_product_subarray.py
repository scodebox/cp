# At each point 3 choice possible
#     1. ith element.
#     2. max -ve before ith * ith element
#     3. max +ve before ith * ith element


# TC: O(n) | SC: O(1)
def solution_1(arr):

    max_product = arr[0]
    min_product = arr[0]
    answer = arr[0]

    for i in range(1, len(arr)):
        choice1 = min_product*arr[i]
        choice2 = max_product*arr[i]

        min_product = min(arr[i], choice1, choice2)
        max_product = max(arr[i], choice1, choice2)
        answer = max(answer, max_product)

    return answer


if __name__ == '__main__':
    arr = [1, -2, -3, 0, 7, -8, -2]  # 112
    # arr = [6, -3, -10, 0, 2]  # 180
    # arr = [-1, -3, -10, 0, 60]  # 60
    # arr = [-2, -40, 0, -2, -3]  # 80
    # arr = [-6, 4, -5, 8, -10, 0, 8]  # 1600

    print('solution_1: ', solution_1(arr))
