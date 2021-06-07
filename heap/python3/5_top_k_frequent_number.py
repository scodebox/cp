import heapq


def k_frequent(nums, k):
    frq = dict()
    heap = []
    heapq.heapify(heap)

    # frequency count
    for item in nums:
        if item in frq:
            frq[item] += 1
        else:
            frq[item] = 1

    # min heap
    for key in frq.keys():
        heapq.heappush(heap, (frq[key], key))
        if len(heap) > k:
            heapq.heappop(heap)

    # return max frequent number
    return [item for _, item in heap]


if __name__ == '__main__':
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    print(k_frequent(arr, k))

    arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k = 4
    print(k_frequent(arr, k))
