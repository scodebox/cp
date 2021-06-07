import heapq


# TC: O(n log k) | SC: O(k)
def k_closest(nums, k, x):
    heap = []

    for item in nums:
        # store the pair of absolute difference and the item in max heap.
        heap.append((abs(item-x), item))
        heapq._heapify_max(heap)

        # pop higher than k
        if len(heap) > k:
            heapq.heappop(heap)

    return [j for _, j in heap]


if __name__ == '__main__':
    arr = [10, 2, 14, 4, 7, 6]  # [2, 3, 5, 6, 8, 9, 10]
    x = 5
    k = 3

    print(k_closest(arr, k, x))
