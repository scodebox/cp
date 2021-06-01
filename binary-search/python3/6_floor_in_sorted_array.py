# floor value is less thand and close to the key


# TC: O(log(N)) | SC: O(1)
def find_floor(nums, key):
    start = 0
    end = len(nums)-1

    floor_value = None

    while start <= end:
        mid = start+((end-start)//2)

        if nums[mid] <= key:
            floor_value = nums[mid]

        if nums[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return floor_value


if __name__ == '__main__':
    arr = [1, 2, 8, 10, 10, 12, 19]

    print(find_floor(arr, 5))
    print(find_floor(arr, 20))
    print(find_floor(arr, 0))
    print(find_floor(arr, 10))

    arr = [1, 2, 4, 6, 10, 12, 14]
    print(find_floor(arr, 7))
