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


# TC: O(log(N)) | SC: O(1)
def count_element(arr, element):
    return (last_occurrence(arr, element)-first_occurrence(arr, element)+1)


if __name__ == '__main__':
    arr1 = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    arr2 = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]

    print(count_element(arr1, 5))
    print(count_element(arr2, 2))
    print(count_element(arr2, 8))
