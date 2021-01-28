from priority_queue.priority_queue_base import PriorityQueueBase
from linked_list.position_list import PositionList
from exceptions import Empty


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create a new empty Priotity Queue."""
        self._data = PositionList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("priority queue is empty")

        small = self._data.first()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)

        return small

    def min(self):
        """Return but do not remove(k, v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
