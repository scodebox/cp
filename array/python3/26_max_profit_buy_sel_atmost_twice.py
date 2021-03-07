# TC: O(n) | SC: O(n)
def solution_1(price):
    profit = [0]*len(price)

    # right to left
    max_price = price[-1]
    for i in range(len(price)-2, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], (max_price-price[i]))

    # left to right
    min_price = price[0]
    for i in range(1, len(price)):
        if min_price > price[i]:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))

    return profit[-1]


if __name__ == '__main__':
    price = [10, 22, 5, 75, 65, 80]  # 87
    # price = [2, 30, 15, 10, 8, 25, 80] # 100
    # price = [100, 30, 15, 10, 8, 25, 80] # 72
    # price = [90, 80, 70, 60, 50] # 0

    print('solution_1: ', solution_1(price))
