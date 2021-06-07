import heapq

# TC: O(n log k) | SC: O(k)


def k_close_origin(points, k):
    heap = []
    for point in points:
        heap.append((point[0]**2+point[1]**2, (point[0], point[1])))
        heapq._heapify_max(heap)

        if len(heap) > k:
            heapq.heappop(heap)

    return [point for _, point in heap]


if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]  # [3, 3], [-2, 4]
    k = 2
    print(k_close_origin(points, k))

    points = [[1, 3], [-2, 2]]  # [[-2, 2]]
    k = 1
    print(k_close_origin(points, k))
