def reverse(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def next_permutation(arr):
    inverse_position = len(arr)-1

    while inverse_position >= 0 and arr[inverse_position-1] >= arr[inverse_position]:
        inverse_position -= 1
    inverse_position -= 1

    if inverse_position >= 0:
        next_greater = len(arr)-1
        while next_greater >= 0 and arr[next_greater] <= arr[inverse_position]:
            next_greater -= 1

        arr[next_greater], arr[inverse_position] = arr[inverse_position], arr[next_greater]

    reverse(arr, inverse_position+1, len(arr)-1)


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 2]  # 1,4,2,3,5
    # arr = [1, 2, 3] # 1,3,2
    # arr = [3, 2, 1] # 1,2,3
    # arr = [1, 1, 5] # 1,5,1
    # arr = [1] # 1

    next_permutation(arr)
    print(arr)
