# TC: O(n) | SC:O(n)
def solution_1(arr):
    # splitting -ve and +ve in different array.
    positive = []
    negative = []
    for item in arr:
        if item < 0:
            negative.append(item)
        else:
            positive.append(item)

    # restoring into input +ve and -ve alternatively.
    index = 0
    while positive and negative:
        arr[index] = positive.pop()
        index += 1
        arr[index] = negative.pop()
        index += 1

    while positive:
        arr[index] = positive.pop()
        index += 1

    while negative:
        arr[index] = negative.pop()
        index += 1


# TC: O(n) | SC:O(1)
# Partition algo of quick sort.
def solution_2(arr):
    # moving +ve right and -ve left of the list using partition algo of quick sort.
    positive_index = partition_by_zero(arr)
    negative_index = 0

    # alternating
    while negative_index < positive_index and positive_index < len(arr) and negative_index < len(arr):
        arr[positive_index], arr[negative_index] = arr[negative_index], arr[positive_index]
        negative_index += 2
        positive_index += 1


def partition_by_zero(arr):
    swap_index = -1
    for i in range(0, len(arr)):
        if arr[i] < 0:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    return swap_index+1


if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # arr = [1, 2, 3, -4, -1, 4]
    # arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    # arr = [9, -3, 5, -2, -8, -6, 1, 3]

    # solution_1(arr)
    solution_2(arr)
    print(arr)
