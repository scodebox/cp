

def solution_1(arr1, arr2, arr3):
    index1 = 0
    index2 = 0
    index3 = 0
    common = []

    while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
        if arr1[index1] == arr2[index2] == arr3[index3]:
            # print(arr1[index1])
            common.append(arr1[index1])
            index1 += 1
            index2 += 1
            index3 += 1
        elif arr1[index1] <= arr2[index2] and arr1[index1] <= arr3[index3]:
            index1 += 1
        elif arr2[index2] <= arr1[index1] and arr2[index2] <= arr3[index3]:
            index2 += 1
        elif arr3[index3] <= arr1[index1] and arr3[index3] <= arr2[index2]:
            index3 += 1

    return common


if __name__ == '__main__':
    # 20, 80
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    # 5, 5
    arr1 = [1, 5, 5]
    arr2 = [3, 4, 5, 5, 10]
    arr3 = [5, 5, 10, 20]

    # 5 15 25
    arr1 = [1, 5, 10, 15, 20, 25, 30]
    arr2 = [3, 4, 5, 10, 15, 25, 30, 38]
    arr3 = [0, 2, 5, 13, 15, 16, 17, 25, 32]

    print('solution_1 : ', solution_1(arr1, arr2, arr3))
