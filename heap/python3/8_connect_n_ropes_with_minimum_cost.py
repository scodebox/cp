import heapq


# TC: O(n log n) | SC: O(1)
def min_cost(ropes):
    # using huffnam code
    heapq.heapify(ropes)

    while len(ropes) > 1:
        heapq.heappush(ropes, heapq.heappop(ropes)+heapq.heappop(ropes))

    return (ropes[0])


if __name__ == '__main__':
    ropes = [1, 4, 3, 2, 5]  # 29
    print(min_cost(ropes))
