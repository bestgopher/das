def unique1(s):
    """Return True if there are no duplicate elements in sequence s."""
    for j in range(len(s)):
        for k in range(j + 1, len(s)):
            if s[j] == s[k]:
                return False  # found duplicate pair
    return True  # if we reach this, elements were unique


def unique2(s):
    """Return True if there are no duplicate elements in sequence s."""
    temp = sorted(s)  # create a sorted copy of s
    for j in range(1, len(temp)):
        if temp[j - 1] == temp[j]:
            return False  # found duplicate pair
    return True  # if reach this, elements were unique
