import heapq


# TC: O(n log n) | SC: O(n)
def frequency_sort(nums):
    frq = dict()
    heap = []

    # frequency count
    for item in nums:
        if item in frq:
            frq[item] += 1
        else:
            frq[item] = 1

    # build max heap based on frequency
    for key in frq.keys():
        heap.append((frq[key], key))

    # print sroted order
    while heap:
        heapq._heapify_max(heap)
        frq, num = heapq.heappop(heap)
        # print(frq, num)

        print((str(num) + ' ')*frq, end='')
    print()


if __name__ == '__main__':
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    frequency_sort(arr)
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    frequency_sort(arr)
