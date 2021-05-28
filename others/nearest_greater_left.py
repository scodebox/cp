from stack import is_empty, top, push, pop


def next_largest_element(arr):
    stack = []
    result = []
    for i in arr:
        while (not is_empty(stack) and (top(stack) <= i)):
            pop(stack)

        if is_empty(stack):
            result.append(-1)
        else:
            result.append(top(stack))
        push(stack, i)

    return result


if __name__ == '__main__':
    arr1 = [1, 3, 0, 0, 1, 2, 4]  # >> - - 3 3 3 3 -
    arr2 = [1, 3, 2, 4]  # >> - - 3 -

    print(next_largest_element(arr1))
    print(next_largest_element(arr2))
