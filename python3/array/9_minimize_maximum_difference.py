def minimize_maximum_difference(arr, k):
    if len(arr) < 2:
        return -1
    # sort the list.
    arr.sort()
    # If we add/subtract k to each every element difference will be same.
    difference = arr[-1]-arr[0]   # one probable solution
    # add k to min element and substract k from max element.
    max = arr[-1]-k
    min = arr[0]+k

    # swap is max < min after add and substract.
    if max < min:
        max, min = min, max

    # for all the intermediate elements.
    for i in range(1, len(arr)-1):
        #  greedy approach.
        #  we can add k or substract k.
        temp_max = arr[i]+k
        temp_min = arr[i]-k

        # If any of those value comes in range of (min -> max) that does not change the difference.
        if (temp_max <= max) or (temp_min >= min):
            continue

        # Outside range (min -> max).
        # update with that value which one add less penalty.
        if abs(max-temp_min) < abs(temp_max-min):
            min = temp_min
        else:
            max = temp_max

    if difference < abs(max-min):
        return difference
    else:
        return abs(max-min)


if __name__ == "__main__":
    arr1 = [1, 15, 10]              # ANS 5
    arr2 = [1, 5, 15, 10]           # ANS 8
    arr3 = [4, 6]                   # ANS 2
    arr4 = [6, 10]                  # ANS 2
    arr5 = [1, 10, 14, 14, 14, 15]  # ANS 5
    arr6 = [1, 2, 3]                # ANS 2

    k1 = 6
    k2 = 3
    k3 = 10
    k4 = 3
    k5 = 6
    k6 = 2

    print(minimize_maximum_difference(arr1, k1))
    print(minimize_maximum_difference(arr2, k2))
    print(minimize_maximum_difference(arr3, k3))
    print(minimize_maximum_difference(arr4, k4))
    print(minimize_maximum_difference(arr5, k5))
    print(minimize_maximum_difference(arr6, k6))