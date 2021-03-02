# TC: O(n^2) | SC: O(1)
def solution_1(arr):
    counter = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                counter += 1
    return counter


# TC: O(n log n) | SC: O(n)
# Using merge method.

def merge(arr, start, mid, end):
    i = start
    j = mid+1
    temp = []
    temp_index = 0
    # Insersion counter.
    count = 0

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        if arr[i] > arr[j]:
            temp.append(arr[j])
            # inversion count
            count += (mid-i+1)
            # print ('>>',count)
            j += 1

    if i > mid:
        while j <= end:
            temp.append(arr[j])
            j += 1

    if j > end:
        while i <= mid:
            temp.append(arr[i])
            i += 1

    for x in range(start, end+1):
        arr[x] = temp[temp_index]
        temp_index += 1

    return count


def solution_2(arr, start=None, end=None):
    count = 0
    if None == start and None == end:
        start = 0
        end = len(arr)-1
    if start >= end:
        return 0

    mid = int((start+end)/2)
    count += solution_2(arr, start, mid)
    count += solution_2(arr, mid+1, end)
    count += merge(arr, start, mid, end)
    return count


if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    # print('solution_1 : ',solution_1(arr))
    print('solution_2 : ', solution_2(arr))
