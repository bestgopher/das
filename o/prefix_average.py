# O(n*n)时间复杂度
def prefix_average1(s):
    """Return list such that, for all j, a[j] equals average of S[0],...., S[j]."""
    n = len(s)
    a = [0.0] * n  # create new list of n zeros

    for j in range(n):
        total = 0
        for i in range(j + 1):  # begin computing s[0]+...+s[j]
            total += s[j]
        a[j] = total / (j + 1)  # record the average

    return a


def prefix_average2(s):
    """Return list such that, for all j, a[j] equals average of s[0],...,s[j]."""
    n = len(s)
    a = [0.0] * n  # create new list of n zeros

    for j in range(n):
        a[j] = sum(s[0:j + 1]) / (j + 1)  # record the average
    return a


def prefix_average3(s):
    """Return list such that, for all j, a[j] equals average of s[0],...,s[j]."""
    n = len(s)
    a = [0.0] * n
    total = 0

    for j in range(n):
        total += s[j]  # update prefix sum to include s[j]
        a[j] = total / (j + 1)  # compute average based on current sum
    return a
