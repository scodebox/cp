
def find_range(nums):
    start = 0
    end = start+1

    while nums[end] < 1:
        start = end+1
        end *= 2

    return start, end


def find_first_occurrence(nums, start, end) -> int:
    while start <= end:
        mid = start+((end-start)//2)

        if 0 == nums[mid]:
            start = mid+1
        elif 1 == nums[mid]:
            if 0 == nums[mid-1]:
                return mid
            else:
                end = mid-1


# TC: O(log(N)) | SC: O(1)
def find_first_one(nums):
    start, end = find_range(nums)
    return find_first_occurrence(nums, start, end)


if __name__ == '__main__':

    nums = [0]*33+[1]*40

    print(find_first_one(nums))
