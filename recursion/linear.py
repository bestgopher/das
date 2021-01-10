def linear_sum(s, n):
    """Return the sum of the first n numbers of sequence s."""
    if n == 0:
        return 0
    return s[-1] + linear_sum(s[:n - 1], n - 1)


def reverse(s, start, stop):
    """Reverse elements in implicits slice s[start, end]"""
    if start < stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        reverse(s, start + 1, stop - 1)


if __name__ == '__main__':
    def main():
        assert 45 == linear_sum(list(range(10)), 10)


    main()
