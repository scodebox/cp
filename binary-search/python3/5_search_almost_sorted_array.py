
# arr[i] may be present at arr[i+1] or arr[i-1].


# TC: O(log(N)) | SC: O(1)
def search(nums, key):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)

        if nums[mid] == key:
            return mid
        if mid < len(nums)-1 and nums[mid+1] == key:
            return mid+1
        if mid > 0 and nums[mid-1] == key:
            return mid-1

        if nums[mid] < key:
            start = mid+2
        else:
            end = mid-2

    return -1


if __name__ == '__main__':
    arr = [10, 3, 40, 20, 50, 80, 70]

    print(search(arr, 40))
    print(search(arr, 10))
    print(search(arr, 70))
    print(search(arr, 90))
