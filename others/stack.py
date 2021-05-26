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
