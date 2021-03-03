# Calculate all prefix sum
#     1 > If any prefix sum repeats -> True
#     2 > If any prefix sum is zero -> True


# TC: O(n) | SC: O(n)
def solution_1(arr):
    sum = 0
    sum_set = set()

    for num in arr:
        sum += num
        if 0 == sum or sum in sum_set:
            return True
        sum_set.add(sum)

    return False


if __name__ == '__main__':
    arr = [4, 2, -3, 1, 6]  # True
    arr = [4, 2, 0, 1, 6]   # True
    arr = [-3, 2, 3, 1, 6]  # False

    print('solution_1: ', solution_1(arr))
