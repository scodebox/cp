def sort(arr):
    # Start index 0.
    start = 0
    # End index
    end = len(arr)-1

    while start <= end:
        # Swap all positive value with last index end & decrease end by 1.
        if arr[start] >= 0:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
        else:
            # If arr[start] is not positive then increase start by 1.
            start += 1


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    sort(arr)
    print(arr)
