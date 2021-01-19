from linked_list.base import _DoublyLinkedBase
from exceptions import Empty


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._header.next.value

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._header.prev.value

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self._delete_node(self._header.next)

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self._delete_node(self._trailer.prev)
