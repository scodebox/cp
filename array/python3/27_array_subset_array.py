# TC: O(n) | SC: O(n)
def solution_1(arr1, arr2):
    hash_table = dict()
    # create hash
    for item in arr1:
        if item not in hash_table:
            hash_table[item] = 1

    # If any item of arr2 is missing the its not subset
    for item in arr2:
        if item not in hash_table:
            return False

    return True


if __name__ == '__main__':
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    # arr1 = [1, 2, 3, 4, 5, 6]
    # arr2 = [1, 2, 4]

    # arr1 = [10, 5, 2, 23, 19]
    # arr2 = [19, 5, 3]

    print('solution_1: ', solution_1(arr1, arr2))
