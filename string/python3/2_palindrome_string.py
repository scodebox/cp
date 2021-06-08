
# TC: O(N) | SC: O(1)
def is_plaindrome(s):
    start = 0
    end = len(s)-1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    s = "abba"
    print(is_plaindrome(s))

    s = "abc"
    print(is_plaindrome(s))
