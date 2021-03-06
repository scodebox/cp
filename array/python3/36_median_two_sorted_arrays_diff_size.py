import sys


# TC: O(m+n) | SC: O((m+n)/2)
def solution_1(arr1, arr2):
    total_length = len(arr1)+len(arr2)
    middle = total_length//2

    temp = []
    index1 = 0
    index2 = 0
    counter = 0

    while index1 < len(arr1) and index2 < len(arr2) and len(temp) < middle+1:
        if arr1[index1] <= arr2[index2]:
            temp.append(arr1[index1])
            index1 += 1
        else:
            temp.append(arr2[index2])
            index2 += 1

    while index2 < len(arr2) and len(temp) < middle+1:
        temp.append(arr2[index2])
        index2 += 1

    while index1 < len(arr1) and len(temp) < middle+1:
        temp.append(arr1[index1])
        index1 += 1

    if total_length % 2:
        return temp[-1]
    else:
        return (temp[-1]+temp[-2])/2


# TC: O(log n) | SC: O(1)
def solution_2(arr1, arr2):
    # arr1 should be smaller one.
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    # partiton into two set with equal size.
    # binary search is used to find the place of partiton.
    low = 0
    high = len(arr1)

    while low <= high:
        # for arr1
        cut1 = (low+high)//2
        # for arr2
        cut2 = ((len(arr1)+len(arr2))//2)-cut1

        # for corner cases
        if 0 == cut1:
            l1 = -sys.maxsize-1
        else:
            l1 = arr1[cut1-1]
        if 0 == cut2:
            l2 = -sys.maxsize-1
        else:
            l2 = arr2[cut2-1]
        if len(arr1) == cut1:
            r1 = sys.maxsize
        else:
            r1 = arr1[cut1]
        if len(arr2) == cut2:
            r2 = sys.maxsize
        else:
            r2 = arr2[cut2]

        # print('--')
        # print(l1)
        # print(l2)
        # print(r1)
        # print(r2)

        # binary search.
        if l1 > r2:
            high = cut1-1
        elif l2 > r1:
            low = cut1+1
        else:
            # median return.
            if (len(arr1)+len(arr2)) % 2:
                # odd
                return min(r1, r2)
            else:
                # even
                return (max(l1, l2)+min(r1, r2))/2


if __name__ == '__main__':
    # 3
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]

    # 11
    # arr1 = [2, 3, 5, 8]
    # arr2 = [10, 12, 14, 16, 18, 20]

    # 6.5
    # arr1 = [1, 5, 8, 10, 18, 20]
    # arr2 = [2, 3, 6, 7]

    # 9.5
    # arr1 = [1, 2, 3]
    # arr2 = [9, 10, 11, 12, 13]

    # 16.0
    # arr1 = [1, 12, 15, 26, 38]
    # arr2 = [2, 13, 17, 30, 45]

    # print('solution_1: ', solution_1(arr1, arr2))
    print('solution_2: ', solution_2(arr1, arr2))
