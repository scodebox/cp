

# TC: O(N) | SC: O(1)
def rev(s):
    start = 0
    end = len(s)-1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(''.join(rev(s)))

    s = ["H", "a", "n", "n", "a", "h"]
    print(''.join(rev(s)))
