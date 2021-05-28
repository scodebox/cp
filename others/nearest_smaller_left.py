from stack import is_empty, top, push, pop


def next_largest_element(arr):
    stack = []
    result = []
    for i in arr:
        while (not is_empty(stack) and (top(stack) >= i)):
            pop(stack)

        if is_empty(stack):
            result.append(-1)
        else:
            result.append(top(stack))
        push(stack, i)

    return result


if __name__ == '__main__':
    arr1 = [4, 5, 2, 10, 8]  # >> -1 4 -1 2 2
    arr2 = [1, 3, 2, 4]  # >> -1 1 1 2

    print(next_largest_element(arr1))
    print(next_largest_element(arr2))
