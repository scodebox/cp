

# TC: O(log(N)) | SC: O(1)
def find_min_index(nums):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)
        # next and previous element of mid
        next = (mid+1) % len(nums)
        prev = (mid+len(nums)-1) % len(nums)

        # if next and prev both greater that mid then it is smallest element
        if nums[mid] < nums[next] and nums[mid] < nums[prev]:
            return mid

        # cutting half
        elif nums[start] < nums[end]:
            end = mid-1
        elif nums[start] > nums[end]:
            start = mid+1
        else:
            return mid


# TC: O(log(N)) | SC: O(1)
def binary_search(nums, key, start, end):
    while start <= end:
        mid = start+((end-start)//2)
        if nums[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return -1


def find_element(nums, key):
    min_index = find_min_index(nums)

    left = binary_search(nums, key, 0, min_index-1)
    right = binary_search(nums, key, min_index, len(nums)-1)

    return left if left != -1 else right


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]

    print(find_element(arr, 0))
    print(find_element(arr, 3))
    print(find_element([1], 0))
