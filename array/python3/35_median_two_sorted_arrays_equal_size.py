# TC: O(n) | SC: O(1)
def solution_1(arr1, arr2):
    middle = len(arr1)-1
    index1 = 0
    index2 = 0
    count = 0

    element1 = 0
    element2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            if count == middle:
                element1 = arr1[index1]
            elif count == middle+1:
                element2 = arr1[index1]
            index1 += 1
        else:
            if count == middle:
                element1 = arr2[index2]
            elif count == middle+1:
                element2 = arr2[index2]
            index2 += 1

        count += 1

    return (element1 + element2)/2


# TC: O(log n) | SC: O(1)
def solution_2(arr1, arr2):
    if len(arr1) == 1:
        return ((arr[0]+arr[0])/2)

    elif len(arr1) == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    else:
        median1 = median(arr1)
        median2 = median(arr2)
        size1 = len(arr1)
        size2 = len(arr2)

        # If median1 > meidan 2 then median in:
        #   Either from 1th element to median1 of arr1.
        #   OR from median2 to last element of arr2.

        if median1 > median2:
            if len(arr1) % 2:
                # odd
                return solution_2(arr1[:size1 // 2 + 1], arr2[size2 // 2:])
            else:
                # even
                return solution_2(arr1[:size1 // 2 + 1], arr2[size2 // 2 - 1:])

        # if median2 > median1 then median in :
        #     Either from median1 to last element of arr1.
        #     OR from 1st element to median2 of arr2.

        else:
            if len(arr1) % 2:
                # odd
                return solution_2(arr1[size1 // 2:], arr2[:size2 // 2 + 1])
            else:
                # even
                return solution_2(arr1[size1 // 2 - 1:], arr2[:size2 // 2 + 1])


def median(arr):
    size = len(arr)
    if size % 2:
        # odd -. arr[mid]
        return (arr[size//2])
    else:
        # even -> (arr[mid]+arr[mid-1] / 2)
        return ((arr[size//2] + arr[size//2-1]) / 2)


if __name__ == '__main__':
    # 16.0
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]

    # 5.0
    # arr1 = [1, 2, 3, 6]
    # arr2 = [4, 6, 8, 10]

    # 2.5
    # arr1 = [1, 3]
    # arr2 = [2, 4]

    # 3.5
    # arr1 = [1, 2, 9]
    # arr2 = [3, 4, 7]

    # print('solution_1: ', solution_1(arr1, arr2))
    print('solution_2: ', solution_2(arr1, arr2))
