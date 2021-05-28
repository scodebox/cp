# TC: O(RxC) | SC: O(R)
def solution(matrix):
    # all first row element will be keys in the dict
    count = dict()
    for item in matrix[0]:
        count[item] = 1

    # key increment when that element is repeated
    for row in range(1, len(matrix)):
        for item in matrix[row]:
            if item in count and count[item] < row+1:
                count[item] += 1

    # return key count == No of rows in matrix
    result = []
    for key in count.keys():
        if count[key] == len(matrix):
            result.append(key)

    return result


if __name__ == '__main__':
    matrix = [[1, 2, 1, 4, 8],
              [3, 7, 8, 5, 1],
              [8, 7, 7, 3, 1],
              [8, 1, 2, 7, 9]]

    print(solution(matrix))
