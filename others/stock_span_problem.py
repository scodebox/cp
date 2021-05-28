from stack import is_empty, top, push, pop


# with nearest greater to left
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
