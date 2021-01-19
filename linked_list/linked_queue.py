from linked_list._node import _Node
from linked_list.base import LinkedListBase
from exceptions import Empty
from typing import Optional


class LinkedQueue(LinkedListBase):
    """ FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        super().__init__()
        self._tail: Optional[_Node] = None

    def _check_empty(self):
        """
        if self is empty, raise Empty exception.
        """
        if self.is_empty():
            raise Empty("Queue is empty.")

    def first(self):
        return self._first()

    def dequeue(self):
        """
        Remove and return the first element of the queue(i.e.,FIFO).
        Raise Empty exception if the queue is empty.
        """
        self._check_empty()
        answer = self._head.value
        head_next = self._head.next
        self._head = None
        self._head = head_next
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1


if __name__ == '__main__':
    q = LinkedQueue()

    for i in range(20):
        q.enqueue(i)

    while not q.is_empty():
        print(q.dequeue())
