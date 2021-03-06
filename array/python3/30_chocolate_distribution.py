# TC: O(n log n) | SC: O(n)
def solution_1(packets, kids):
    # sort
    packets.sort()
    start = 0
    end = kids-1
    min_diff = packets[-1]-packets[0]

    # Check all possible subarry for min difference.
    while end < len(packets):
        min_diff = min(min_diff, (packets[end]-packets[start]))
        start += 1
        end += 1

    return min_diff


if __name__ == '__main__':
    packets = [3, 4, 1, 9, 56, 7, 9, 12]
    kids = 5

    # packets = [7, 3, 2, 4, 9, 12, 56]
    # kids = 3

    # packets = [7, 3, 2, 4, 9, 12, 56]
    # kids = 3

    # packets = [3, 4, 1, 9, 56, 7, 9, 12]
    # kids = 5

    # packets = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    # kids = 7

    print('solution_1: ', solution_1(packets, kids))
