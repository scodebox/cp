

# number of rotation == min index

# TC: O(log(N)) | SC: O(1)
def rotation_count(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+((end-start)//2)
        # next and previous element of mid
        next = (mid+1) % len(arr)
        prev = (mid+len(arr)-1) % len(arr)

        # if next and prev both greater that mid then it is smallest element
        if arr[mid] < arr[next] and arr[mid] < arr[prev]:
            return mid

        # cutting half
        elif arr[start] < arr[end]:
            end = mid-1
        elif arr[start] > arr[end]:
            start = mid+1
        else:
            return mid


if __name__ == '__main__':
    arr = [15, 18, 2, 3, 6, 12]
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [7, 9, 11, 12, 5]
    arr = [4, 5, 6, 7, 0, 1, 2]

    print(rotation_count(arr))
