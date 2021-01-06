def rotate(arr):
    last_item = arr[-1]

    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]

    arr[0] = last_item


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    rotate(arr)
    print(arr)
    rotate(arr)
    print(arr)
    rotate(arr)
    print(arr)
    rotate(arr)
    print(arr)
