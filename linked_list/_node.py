from typing import Optional


class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""

    __slots__ = ["_element", "_next"]  # streamline memory usage

    def __init__(self, element, next_node):  # initialize node's fields
        self._element = element  # reference to user's element
        self._next: Optional[_Node] = next_node  # reference to next node

    @property
    def value(self):
        """Return the element."""
        return self._element

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n


class _DoubleNode:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = ["_element", "_prev", "_next"]

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next

    @property
    def value(self):
        """Return the element."""
        return self._element

    @value.setter
    def value(self, v):
        self._element = v

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, n):
        self._prev = n
