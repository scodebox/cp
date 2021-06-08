
def find_duplicate(s):
    frq = dict()
    for ch in s:
        if ch in frq:
            frq[ch] += 1
        else:
            frq[ch] = 1

    for key in frq.keys():
        if frq[key] > 1:
            print('Char : %s -> %d' % (key, frq[key]))


if __name__ == '__main__':
    s = "suvam basak"
    find_duplicate(s)
