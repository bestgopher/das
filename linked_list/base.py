from linked_list._node import _Node, _DoubleNode
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


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    def __init__(self):
        """Create an empty list."""
        self._header = _DoubleNode(None, None, None)
        self._trailer = _DoubleNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of the element in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = _DoubleNode(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _DoubleNode):
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node.prev
        successor = node.next

        predecessor.next = successor
        successor.prev = predecessor

        self._size -= 1

        element = node.value
        node.prev = node.next = node.value = None

        return element
