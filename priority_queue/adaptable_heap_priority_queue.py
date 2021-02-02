from priority_queue.heap_priority_queue import HeadPriorityQueue


class AdaptableHeapPriorityQueue(HeadPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    class Locator(HeadPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = "_index"

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        super(AdaptableHeapPriorityQueue, self)._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._up_heap(j)
        else:
            self._down_heap(j)

    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._up_heap(len(self._data) - 1)
        return token

    def update(self, loc: Locator, new_key, new_val):
        """Update the key and value for the entry identified by Locator loc"""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("invalid locator")

        loc._key = new_key
        loc._value = new_val
        self._bubble(j)

    def remove(self, loc: Locator):
        """Remove and return the (k, v) pair identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("invalid locator")

        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)
