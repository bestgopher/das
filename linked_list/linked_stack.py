from typing import Optional
from linked_list._node import _Node
from exceptions import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty stack."""
        self._head: Optional[_Node] = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of stack."""
        self._head = _Node(e, self._head)  # create and link a new head
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty.")

        return self._head.value

    def pop(self):
        """
        Remove and return the element from the top of the stack(i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty.")

        value = self._head.value
        self._head = self._head.next
        self._size -= 1

        return value
