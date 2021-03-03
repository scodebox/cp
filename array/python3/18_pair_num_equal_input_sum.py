# TC: O(n^2) | SC: O(1)
def solution_1(arr, sum):
    count = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                print('(', arr[i], ',', arr[j], ')')
                count += 1
    return count


# TC: O(n) | SC: O(1)
def solution_2(arr, sum):
    count = 0
    hash_table = dict()

    for key in arr:
        if key in hash_table:
            hash_table[key] = hash_table[key]+1
        else:
            hash_table[key] = 1

    for num in arr:
        key = sum-num
        if key in hash_table:
            count += hash_table[key]
            print('(', num, ',', key, ')', ' -> ', hash_table[key], 'pairs')
        if num in hash_table:
            del hash_table[num]

    return count


if __name__ == '__main__':
    arr = [1, 5, 7, -1]  # (1, 5) and (7, -1)
    sum = 6

    # arr = [1, 5, 7, -1, 5]  # (1, 5), (7, -1) & (1, 5)
    # sum = 6

    # arr = [1, 1, 1, 1]  # total 6
    # sum = 2

    # arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
    # sum = 11

    print('solution_1 : ', solution_1(arr, sum))
    print('solution_2 : ', solution_2(arr, sum))