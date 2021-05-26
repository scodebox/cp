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


def stock_span_problem(arr):
    stack = []
    result = []
    for i in range(0, len(arr)):
        while (not is_empty(stack) and (arr[top(stack)] <= arr[i])):
            pop(stack)

        if is_empty(stack):
            result.append(1)
        else:
            result.append(i-top(stack))
        push(stack, i)

    return result


if __name__ == '__main__':
    arr1 = [100, 80, 60, 70, 60, 75, 85]  # >> 1, 1, 1, 2, 1, 4, 6

    print(stock_span_problem(arr1))
