from priority_queue.priority_queue_base import PriorityQueueBase
from exceptions import Empty


class HeadPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    @staticmethod
    def _parent(j):
        return (j - 1) // 2

    @staticmethod
    def _left(j):
        return 2 * j + 1

    @staticmethod
    def _right(j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)

    def _has_right(self, j):
        return self._right(j) < len(self.data)

    def _swap(self, i, j):
        """Swap the elements indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _uphead(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._uphead(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self):
        """"Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        item = self._Item(key, value)
        self._data.append(item)
        self._uphead(len(self._data) - 1)

    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("priority queue is empty")

        return (self._data[0]._key, self._data[0]._value)

    def remove_min(self):
        """
        Return and  remove (k, v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("priority queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
