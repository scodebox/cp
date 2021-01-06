# using modified merge function
def compute_union(arr1, arr2):
    union = []
    index1 = 0
    index2 = 0

    while (index1 < len(arr1)) and (index2 < len(arr2)):
        if arr1[index1] < arr2[index2]:
            union.append(arr1[index1])
            index1 += 1
        elif arr1[index1] > arr2[index2]:
            union.append(arr2[index2])
            index2 += 1
        else:
            union.append(arr2[index2])
            index1 += 1
            index2 += 1

    while index1 < len(arr1):
        union.append(arr1[index1])
        index1 += 1
    while index2 < len(arr2):
        union.append(arr2[index2])
        index2 += 1

    return union


# using modified merge function
def compute_intersection(arr1, arr2):
    intersection = []
    index1 = 0
    index2 = 0

    while (index1 < len(arr1)) and (index2 < len(arr2)):
        if arr1[index1] < arr2[index2]:
            index1 += 1
        elif arr1[index1] > arr2[index2]:
            index2 += 1
        else:
            intersection.append(arr2[index2])
            index1 += 1
            index2 += 1

    return intersection


if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    # arr1=[2, 5, 6]
    # arr2=[4, 6, 8, 10]
    union = compute_union(arr1, arr2)
    print('union : ', union)
    intersection = compute_intersection(arr1, arr2)
    print('intersection : ', intersection)
