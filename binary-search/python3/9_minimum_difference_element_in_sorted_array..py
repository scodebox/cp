
def min_difference(nums, key) -> int:
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)

        if nums[mid] == key:
            return nums[mid]
        elif nums[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return (nums[start] if abs(nums[start]-key) < abs(nums[end]-key) else nums[end])


if __name__ == '__main__':
    arr = [1, 2, 8, 10, 12, 15]
    print(min_difference(arr, 12))

    arr = [1, 2, 8, 10, 13, 15]
    print(min_difference(arr, 12))
    print(min_difference(arr, 3))
