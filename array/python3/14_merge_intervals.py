# TC: O(n log n ) | SC: O(n)
def solution_1(intervals):
    # non decreasing order sorting based on interval start.
    intervals.sort(key=lambda x: x[0])

    stack = []
    for interval in intervals:
        # stack not empty.
        if stack:
            # check overlapping interval.
            stack_top = stack.pop()
            x1, x2 = stack_top
            y1, y2 = interval

            if x1 <= y1 and y1 <= x2:
                if y2 <= x2:
                    stack.append(stack_top)
                elif x2 < y2:
                    new_interval = []
                    new_interval.append(x1)
                    new_interval.append(y2)
                    stack.append(new_interval)
            else:
                stack.append(interval)
        # stack empty.
        else:
            stack.append(interval)

    return stack


if __name__ == '__main__':
    intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
    print(solution_1(intervals))
