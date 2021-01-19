from linked_list._node import _Node
from typing import Optional
from exceptions import Empty


class LinkedListBase:
    """Linked list base object"""

    def __init__(self):
        self._head: Optional[_Node] = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linked-list."""
        return self._size

    def is_empty(self):
        """Return True if the linked-list is empty."""
        return self._size == 0

    def _first(self):
        """
        Return (but do not remove) the element at the top of the linked-list.
        Raise Empty exception if the linked-list is empty.
        """
        self._check_empty()
        return self._head.value

    def _check_empty(self):
        """
        if self is empty, raise Empty exception.
        """
        if self.is_empty():
            raise Empty("Linked-list is empty.")
