# TC: O(n) | SC: O(n)
def solution_1(nums, k):
    # Hash table to keep count of each number.
    hash_table = dict()
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    # Checking the number appear more than 9n/k) times.
    for key in hash_table.keys():
        if hash_table[key] > (len(nums)//k):
            print(key)


if __name__ == '__main__':
    nums = [1, 2, 6, 6, 6, 6, 6, 10]  # 6
    k = 4
    # nums = [3, 4, 4, 5, 5, 5, 5]  # 4 5
    # k = 4
    # nums = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]  # 1 2
    # k = 4

    solution_1(nums, k)
