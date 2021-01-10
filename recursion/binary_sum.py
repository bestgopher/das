def binary_sum(s, start, stop):
    """Return the sum of the numbers in implicit slice s[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)
