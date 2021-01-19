from linked_list._node import _Node
from linked_list.base import LinkedListBase
from exceptions import Empty


class LinkedStack(LinkedListBase):
    """LIFO Stack implementation using a singly linked list for storage."""

    def _check_empty(self):
        """
        if self is empty, raise Empty exception.
        """
        if self.is_empty():
            raise Empty("Stack is empty.")

    def push(self, e):
        """Add element e to the top of stack."""
        self._head = _Node(e, self._head)  # create and link a new head
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        return self._first()

    def pop(self):
        """
        Remove and return the element from the top of the stack(i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        self._check_empty()

        value = self._head.value
        self._head = self._head.next
        self._size -= 1

        return value


if __name__ == '__main__':
    l = LinkedStack()
    for i in range(10):
        l.push(i)

    while not l.is_empty():
        print(l.pop())
