from priority_queue.priority_queue_base import PriorityQueueBase
from linked_list.position_list import PositionList
from exceptions import Empty


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priotity Queue."""
        self._data = PositionList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove(k, v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("priority queue is empty")

        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("priority queue is empty")

        item = self._data.delete(self._data.first())
        return (item._key, item._value)
