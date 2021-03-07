# TC: O(n) | SC: O(1)
def solution_1(arr):
    # Get the max height.
    max_height_index = 0
    for i in range(0, len(arr)):
        if arr[max_height_index] < arr[i]:
            max_height_index = i

    water = 0
    # calculate the left of the max height.
    index = 1
    max_height_index_2 = 0

    while index < max_height_index:
        water_level = min(arr[max_height_index], arr[max_height_index_2])

        if arr[index] < water_level:
            water += water_level-arr[index]

        if arr[max_height_index_2] < arr[index]:
            max_height_index_2 = index
        index += 1

    # Calculate the right of the max height.
    index = len(arr)-2
    max_height_index_2 = len(arr)-1

    while index > max_height_index:
        water_level = min(arr[max_height_index], arr[max_height_index_2])

        if arr[index] < water_level:
            water += water_level-arr[index]

        if arr[max_height_index_2] < arr[index]:
            max_height_index_2 = index
        index -= 1

    return water


if __name__ == '__main__':
    arr = [3, 0, 0, 2, 0, 4]  # 10
    # arr = [7, 4, 0, 9]  # 10
    # arr = [6, 9, 9]  # 0
    # arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    # arr = [1,0,0,5,0,0,1] # 4

    print('solution_1: ', solution_1(arr))
