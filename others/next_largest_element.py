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


def next_largest_element(arr):
    stack = []
    result = []
    for i in range(len(arr)-1, -1, -1):
        while (not is_empty(stack) and (top(stack) <= arr[i])):
            pop(stack)

        if is_empty(stack):
            result.append(-1)
        else:
            result.append(top(stack))
        push(stack, arr[i])

    result.reverse()
    return result


if __name__ == '__main__':
    arr1 = [1, 3, 0, 0, 1, 2, 4]  # >> 3 4 1 1 2 4 -1
    arr2 = [1, 3, 2, 4]  # >> 3 4 4 -1

    print(next_largest_element(arr1))
    print(next_largest_element(arr2))
