
# TC: O(log(N)) | SC: O(1)


def find_range(nums, key):
    start = 0
    end = start+1

    while key > nums[end]:
        start = end+1
        end *= 2  # assumed infinite

    return start, end


def binary_search(nums, key, start, end) -> int:
    while start <= end:
        mid = start+((end-start)//2)
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return -1


def search(nums, key):
    start, end = find_range(nums, key)
    return binary_search(nums, key, start, end)


if __name__ == '__main__':

    nums = [item+1 for item in range(500)]

    print(search(nums, 250))
