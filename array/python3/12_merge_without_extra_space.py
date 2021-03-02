import math

# TC: O(mxn) | SC: O(1)


def solution_1(arr_1, arr_2):
    index_1 = 0
    index_2 = 0

    while index_1 < len(arr_1):
        if arr_1[index_1] >= arr_2[index_2]:
            arr_1[index_1], arr_2[index_2] = arr_2[index_2], arr_1[index_1]
            # After each swap sort the arr_2.
            arr_2.sort()
        else:
            index_1 += 1


# TC: O(n log n) | SC: O(1) :: Gap Method
def solution_2(arr_1, arr_2):
    # calculating gap. [(size 1 + size 2)/2]
    gap = math.ceil((len(arr_1)+len(arr_2))/2)

    # Do this till gap = 1.
    while gap >= 1:
        for index in range(0, (len(arr_1)+len(arr_2))-gap):
            # print (index, index+gap)

            # index and list decode.
            if index >= len(arr_1):
                first_index = index-len(arr_1)
                first_flag = True
            else:
                first_index = index
                first_flag = False

            if index+gap >= len(arr_1):
                last_index = (index+gap)-len(arr_1)
                last_flag = True
            else:
                last_index = (index+gap)
                last_flag = False

            # Swaps
            # both index in first list.
            if (False == first_flag) and (False == last_flag):
                if arr_1[first_index] > arr_1[last_index]:
                    arr_1[first_index], arr_1[last_index] = arr_1[last_index], arr_1[first_index]

            # first index in list_1 and last index in list_2.
            elif (False == first_flag) and (True == last_flag):
                if arr_1[first_index] > arr_2[last_index]:
                    arr_1[first_index], arr_2[last_index] = arr_2[last_index], arr_1[first_index]

            # both index in last list.
            elif (True == first_flag) and (True == last_flag):
                if arr_2[first_index] > arr_2[last_index]:
                    arr_2[first_index], arr_2[last_index] = arr_2[last_index], arr_2[first_index]

        # Because of ceil value gap would not become 0. So when operation of gap = 1 is done break the loop.
        if 1 == gap:
            break
        else:
            gap = math.ceil(gap/2)


if __name__ == '__main__':
    arr_1 = [10]
    arr_2 = [2, 3]

    arr_1 = [1, 4, 7, 8, 10]
    arr_2 = [2, 3, 9]

    arr_1 = [1, 5, 9, 10, 15, 20]
    arr_2 = [2, 3, 8, 13]

    arr_1 = [3, 4, 7, 10]
    arr_2 = [1, 2, 8, 9, 12, 13]

    # print("solution_1 :")
    # solution_1(arr_1, arr_2)
    # print(arr_1)
    # print(arr_2)

    print("solution_2 :")
    solution_2(arr_1, arr_2)
    print(arr_1)
    print(arr_2)
