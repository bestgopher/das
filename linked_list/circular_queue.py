from typing import Optional
from exceptions import Empty
from linked_list.base import LinkedListBase
from linked_list._node import _Node


class CircularQueue(LinkedListBase):
    """Queue implementation using class for storing a singly linked node."""

    def __init__(self):
        """Create an empty queue."""
        self._tail: Optional[_Node] = None
        self._size = 0

    def _check_empty(self):
        if self.is_empty():
            raise Empty("Queue is empty")

    def first(self):
        """
        Return(but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        self._check_empty()
        head = self._tail.next
        return head.value

    def dequeue(self):
        """
        Remove and return the first element of the queue(i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        self._check_empty()
        answer = self._tail.next

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = answer.next

        self._size -= 1
        return answer.value

    def enqueue(self, e):
        """Add an element to the back of queue."""
        node = _Node(e, None)
        if self.is_empty():
            self._tail = node
            self._tail._next = node
        else:
            node._next = self._tail.next
            self._tail._next = node
            self._tail = node

        self._size += 1


if __name__ == '__main__':
    q = CircularQueue()

    for i in range(20):
        q.enqueue(i)

    while not q.is_empty():
        print(q.dequeue())
