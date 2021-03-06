# TC: O(n^2) | SC: O(1)
def solution_1(arr, value):
    # sort
    arr.sort()

    # search for triplet
    for start in range(0, len(arr)-2):
        end = len(arr)-1
        mid = start+1

        while mid < end:
            if (arr[start]+arr[mid]+arr[end]) == value:
                print(arr[start], arr[mid], arr[end])
                return True
            elif (arr[start]+arr[mid]+arr[end]) < value:
                mid += 1
            else:
                end -= 1

    return False


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, 8]
    value = 13

    # arr = [1, 2, 4, 3, 6]
    # value = 10

    # arr = [12, 3, 4, 1, 6, 9]
    # value = 24

    # arr = [1, 2, 3, 4, 5]
    # value = 9

    print('solution_1: ', solution_1(arr, value))
