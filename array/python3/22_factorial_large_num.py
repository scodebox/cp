def multiply(m, result):
    carry = 0

    for i in range(0, len(result)):
        temp = (result[i]*m) + carry
        result[i] = temp % 10
        carry = temp//10

    while carry:
        result.append(carry % 10)
        carry = carry//10


def fact(num):
    result = []
    result.append(1)
    for i in range(2, num+1):
        multiply(i, result)

    for i in range(len(result)-1, -1, -1):
        print(result[i], end='')


if __name__ == '__main__':
    num = 100000
    fact(num)
