# TC: O(n log n) | SC: O(1)
def solution_1(nums):
    nums.sort()
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        # count as long as the current (value - 1) exist.
        if nums[i]-1 == nums[i-1]:
            current += 1
        else:
            # When (value - 1) not there start a new sequence.
            current = 1

        # Take the max sequence.
        longest = max(longest, current)

    return longest


# TC: O(n) | SC: O(n)
def solution_2(nums):
    # Create a set of all numbers.
    hash_set = set()
    for num in nums:
        hash_set.add(num)

    longest = 0
    current = 0
    for num in nums:
        # Go until the minimum number of a existing sequence.
        if (num-1) not in hash_set:
            current_number = num

            # Start from the minimum number of existing sequence untill the end.
            while current_number in hash_set:
                current += 1
                current_number += 1

            # Take the max sequence & reset the current value to calculate next sequence length.
            longest = max(longest, current)
            current = 0

    return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]  # 4
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # 9
    # nums = [1, 9, 3, 10, 4, 20, 2]  # 4
    # nums = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]  # 5
    # nums = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]  # 6

    # print('solution_1: ', solution_1(nums))
    print('solution_1: ', solution_2(nums))
