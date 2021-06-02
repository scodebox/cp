
def binary_search(nums, key, start, end, order=True):
    while start <= end:
        mid = start+((end-start)//2)
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            if order:
                start = mid+1
            else:
                end = mid-1
        else:
            if order:
                end = mid-1
            else:
                start = mid+1
    return -1


def find_max(nums):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif (mid > 0 and nums[mid] > nums[mid-1]) or (mid < len(nums)-1 and nums[mid] < nums[mid+1]):
            start = mid+1
        else:
            end = mid-1


def search(nums, key):
    max_index = find_max(nums)
    left = binary_search(nums, key, 0, max_index)
    right = binary_search(nums, key, max_index, len(nums)-1, order=False)

    return (left if left != -1 else right)


if __name__ == '__main__':
    # arr = [1, 4, 8, 3, 2]
    # print(search(arr))

    arr = [1, 2, 3, 5, 8, 3, 2]
    print(search(arr, 3))

    arr = [5, 10, 9, 7, 4, 3, 2]
    print(search(arr, 3))
