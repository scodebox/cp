# TC: O(n) | SC: O(n)
def solution_1(arr):
    frequency_count = [0]*len(arr)
    for i in arr:
        frequency_count[i] += 1
        # when frequency of a number is more than 1 return that number.
        if frequency_count[i] > 1:
            return i
    # no duplicate number.
    return None


# Floyd's Tortoise and Hare (Cycle Detection)
# TC: O(n) | SC: O(1)
def solution_2(arr):
    fast = slow = arr[0]

    fast = arr[arr[fast]]
    slow = arr[slow]
    while fast != slow:
        fast = arr[arr[fast]]
        slow = arr[slow]

    fast = arr[0]
    while fast != slow:
        slow = arr[slow]
        fast = arr[fast]

    return fast


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 2]  # 2
    # arr = [3, 1, 3, 4, 2]  # 3
    # arr = [1, 1]  # 1
    # arr = [1, 1, 2]  # 1

    print("solution_1 : {}".format(solution_1(arr)))
    print("solution_2 : {}".format(solution_2(arr)))
