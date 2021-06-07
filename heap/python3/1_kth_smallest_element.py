import heapq


def find_kth_smallest(nums, k):
    heap = []

    for item in nums:
        heap.append(item)
        heapq._heapify_max(heap)
        if len(heap) > k:
            heapq.heappop(heap)

    heapq._heapify_max(heap)
    return heapq.heappop(heap)


if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]  # 7
    k = 3

    print(find_kth_smallest(arr, k))
