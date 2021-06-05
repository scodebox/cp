import heapq


# TC: O(n log k) | SC: O(k)
def sort(nums, k):
    heap = []
    heapq.heapify(heap)

    for item in nums:
        heapq.heappush(heap, item)
        if len(heap) > k:
            print(heapq.heappop(heap), end=' ')

    while heap:
        print(heapq.heappop(heap), end=' ')
    print()


if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9]  # [2, 3, 5, 6, 8, 9, 10]
    k = 3

    sort(arr, k)
