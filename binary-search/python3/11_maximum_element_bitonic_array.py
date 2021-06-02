

# TC: O(log(N)) | SC: O(1)
def find_max(nums):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start+((end-start)//2)

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid]
        elif (mid > 0 and nums[mid] > nums[mid-1]) or (mid < len(nums)-1 and nums[mid] < nums[mid+1]):
            start = mid+1
        else:
            end = mid-1


if __name__ == '__main__':
    arr = [1, 4, 8, 3, 2]
    print(find_max(arr))

    arr = [1, 2, 3, 5, 8, 3, 2]
    print(find_max(arr))

    arr = [5, 10, 9, 7, 4, 3, 2]
    print(find_max(arr))
