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
