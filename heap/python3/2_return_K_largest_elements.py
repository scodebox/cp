import heapq


def get_k_largest(nums, k):
    heap = []
    heapq.heapify(heap)
    for item in nums:
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap


if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]  # 7
    k = 3

    print(get_k_largest(arr, k))
