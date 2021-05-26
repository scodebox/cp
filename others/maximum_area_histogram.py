from stack import is_empty, top, push, pop


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
            left.append(0)
        else:
            left.append(top(stack))
        push(stack, i)

    stack = []
    # nearest smaller right
    for i in range(len(histogram)-1, -1, -1):
        while (not is_empty(stack) and (histogram[top(stack)] >= histogram[i])):
            pop(stack)

        if is_empty(stack):
            right.append(len(histogram)-1)
        else:
            right.append(top(stack))
        push(stack, i)

    right.reverse()
    # max area
    for i in range(0, len(histogram)):
        max_area = max(max_area, (right[i]-left[i]-1)*histogram[i])

    return max_area


if __name__ == '__main__':
    h = [6, 2, 5, 4, 5, 1, 6]  # 12
    print(maximum_area_histogram(h))
