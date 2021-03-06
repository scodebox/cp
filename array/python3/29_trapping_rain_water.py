# TC: O(n) | SC: O(1)
def solution_1(arr):
    water = 0
    for i in range(1, len(arr)-1):
        water_level = min(max(arr[0:i]), max(arr[i+1:]))
        if water_level > arr[i]:
            water += water_level-arr[i]

    return water


if __name__ == '__main__':
    arr = [3, 0, 0, 2, 0, 4]  # 10
    arr = [7, 4, 0, 9]  # 10
    arr = [6, 9, 9]  # 0
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6

    print('solution_1: ', solution_1(arr))
