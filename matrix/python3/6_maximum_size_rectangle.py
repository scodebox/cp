# using max area of histogram
def is_empty(stack):
    if len(stack):
        return False
    return True


def push(stack, item):
    stack.append(item)


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None


def top(stack):
    if len(stack):
        return stack[-1]
    return None


def maximum_area_histogram(histogram):
    max_area = 0
    stack = []
    left = []
    right = []
    # nearest smaller left
    for i in range(0, len(histogram)):
        while (not is_empty(stack) and (histogram[top(stack)] >= histogram[i])):
            pop(stack)

        if is_empty(stack):
            left.append(-1)
        else:
            left.append(top(stack))
        push(stack, i)

    stack = []
    # nearest smaller right
    for i in range(len(histogram)-1, -1, -1):
        while (not is_empty(stack) and (histogram[top(stack)] >= histogram[i])):
            pop(stack)

        if is_empty(stack):
            right.append(len(histogram))
        else:
            right.append(top(stack))
        push(stack, i)

    right.reverse()

    # print(left)
    # print(right)
    # max area
    for i in range(0, len(histogram)):
        max_area = max(max_area, (right[i]-left[i]-1)*histogram[i])

    return max_area


# TC: O(RxC) | SC: O(C)
def get_max_area(grid):
    # compress to histogram.
    histogram = [0]*len(grid[0])
    max_area = 0
    # get max of each histogram
    for row in grid:
        index = 0
        for item in row:
            if item:
                histogram[index] += item
            else:
                histogram[index] = 0
            index += 1

        max_area = max(max_area, maximum_area_histogram(histogram))
    return max_area


if __name__ == '__main__':
    grid = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]  # 8
    grid = [[0, 1, 1], [1, 1, 1], [0, 1, 1]]  # 6
    grid = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]  # 6

    print(get_max_area(grid))
