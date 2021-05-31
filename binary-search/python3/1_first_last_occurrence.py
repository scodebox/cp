# TC: O(log(N)) | SC: O(1)
def last_occurrence(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+((end-start)//2)
        if arr[mid] == key and (mid == len(arr)-1 or arr[mid+1] > key):
            return mid
        elif arr[mid] > key:
            end = mid-1
        else:
            start = mid+1

# TC: O(log(N)) | SC: O(1)


def first_occurrence(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+((end-start)//2)

        if arr[mid] == key and (mid == 0 or arr[mid-1] < key):
            return mid
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1


if __name__ == '__main__':
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    key = 8
    print(first_occurrence(arr, key))
    print(last_occurrence(arr, key))
