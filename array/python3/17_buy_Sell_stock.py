# TC: O(n^2) | SC: (1)
def solution_1(prices):
    max_profit = 0

    for i in range(0, len(prices)-1):
        for j in range(1, len(prices)):
            if prices[j]-prices[i] > max_profit:
                max_profit = prices[j]-prices[i]

    return max_profit


# TC: O(n) | SC: (1)
def solution_2(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(0, len(prices)):
        if min_price > prices[i]:
            min_price = prices[i]
        else:
            if prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]  # 5

    print('solution_1 : ', solution_1(prices))
    print('solution_2 : ', solution_2(prices))
