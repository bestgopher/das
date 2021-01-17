from stack_queue.exceptions import Empty
from stack_queue.queue_base import BaseQueue


class ArrayQueue(BaseQueue):
    """FIFO queue implementation using a Python list as underlying storage."""

    def first(self):
        """
        Return(but do not remove) the element at the front of the queue.
        Raise Empty exception of the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue(i.e., FIFO).
        Raise Empty exception of the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")

        if len(self._data) // self._size >= 4:
            self._resize(len(self._data) // 2)

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, t):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = t
        self._size += 1


if __name__ == '__main__':

    queue = ArrayQueue()

    for i in range(30):
        queue.enqueue(i)

    while not queue.is_empty():
        print(queue.dequeue())
