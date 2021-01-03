def find_max_min(l):
    if not l:
        return (-1, -1)

    max = l[0]
    min = l[0]

    for item in l:
        if item > max:
            max = item
        elif item < min:
            min = item

    return (max, min)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = []
    max_min = find_max_min(l)
    print(max_min)
