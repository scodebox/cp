import heapq as heap


# TC: O(N^2) | SC: O(1)
def solution_1(m):
    # push all elements into the min heap
    min_heap = []
    for row in m:
        for element in row:
            heap.heappush(min_heap, element)

    # return sorted element
    return [heap.heappop(min_heap) for i in range(len(min_heap))]


if __name__ == '__main__':
    m = [[10, 20, 30, 40], [15, 25, 35, 45],
         [27, 29, 37, 48], [32, 33, 39, 50]]

    m = [[1, 5, 3], [2, 8, 7], [4, 6, 9]]

    print('solution_1: ', solution_1(m))
