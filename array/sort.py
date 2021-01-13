def insert_sort(s):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(s)):
        while k > 0:
            if s[k] > s[k - 1]:
                break
            s[k], s[k - 1] = s[k - 1], s[k]
            k -= 1


if __name__ == '__main__':
    s = [231, 53, 12, 431, 5, 13, 2]
    insert_sort(s)
    print(s)
