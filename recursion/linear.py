def linear_sum(s, n):
    """Return the sum of the first n numbers of sequence s."""
    if n == 0:
        return 0
    return s[-1] + linear_sum(s[:n - 1], n - 1)


if __name__ == '__main__':
    def main():
        assert 45 == linear_sum(list(range(10)), 10)


    main()
