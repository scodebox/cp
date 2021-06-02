

# TC: O(log(N)) | SC: O(1)
def find_peak(nums):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)

        # first element
        if mid == 0 and nums[mid] > nums[mid+1]:
            return mid
        # last element
        elif mid == len(nums)-1 and nums[mid] > nums[mid-1]:
            return mid
        # middle
        elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            start = mid+1
        else:
            end = mid-1


if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    print(find_peak(arr))

    arr = [1, 2, 1, 3, 5, 6, 4]
    print(find_peak(arr))
