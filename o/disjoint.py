def disjoint1(a, b, c):
    """Return True if there is no element common to all three lists."""
    for i in a:
        for j in b:
            for k in c:
                if i == j == k:
                    return False  # we found a common value

    return True  # if we reach this, sets are disjoint


def disjoint2(a, b, c):
    """Return True if there is no element common to all three lists."""
    for i in a:
        for j in b:
            if i == j:  # only check c if we found match from a and b.
                return False

            for k in c:
                if i == k:  # (and thus i == j == k)
                    return False  # we found a common value

    return True  # if we reach this, sets are disjoint
