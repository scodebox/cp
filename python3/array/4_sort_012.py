def sort(arr):
    # Low at first index.
    low = 0
    # High at last index.
    high = len(arr)-1
    # Mid ar first index. Will be moving towards high.
    mid = 0

    while mid <= high:
        if arr[mid] == 0:
            # When the mid index value is 0 -> swap with low.
            arr[mid], arr[low] = arr[low], arr[mid]
            # Increase the low and mid index by one.
            mid += 1
            low += 1
        elif arr[mid] == 1:
            # If the mid index value is 1 just move to next index.
            mid += 1
        elif arr[mid] == 2:
            # If the mid index value is 2 -> swap with high index.
            arr[mid], arr[high] = arr[high], arr[mid]
            # Decrease the high index by 1. DONT do anything to mid index.
            high -= 1


if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sort(arr)
    print(arr)
