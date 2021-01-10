def unique3(s, start, stop):
    """Return True if there are no duplicates elements in slice s[start:stop]."""

    if stop - start <= 0:  # at most one item
        return True
    elif not unique3(s, start, stop - 1):  # first part has duplicate
        return False
    elif not unique3(s, start + 1, stop):  # second part has duplicate
        return False
    else:
        return s[start] != s[stop - 1]  # do first and last differ?

