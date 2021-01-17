from stack_queue.exceptions import Empty
from stack_queue.queue_base import BaseQueue


class ArrayDeque(BaseQueue):

    def add_first(self, t):
        if self._size == len(self._data):
            self._resize(2 * self._size)

        front = (self._front - 1) % len(self._data)
        self._data[front] = t
        self._front = front
        self._size += 1

    def add_last(self, t):
        if self._size == len(self._data):
            self._resize(2 * self._size)

        last = (self._front + self._size - 1) % len(self._data)
        self._data[last] = t
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        if len(self._data) // self._size >= 4:
            self._resize(len(self._data) // 2)

        data = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return data

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        if len(self._data) // self._size >= 4:
            self._resize(len(self._data) // 2)

        last = (self._front + self._size - 1) % len(self._data)
        data = self._data[last]
        self._data[last] = None
        self._size -= 1

        return data

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._data[(self._front + self._size - 1) % len(self._data)]


if __name__ == '__main__':
    d = ArrayDeque()

    for i in range(20):
        d.add_first(i)
    while not d.is_empty():
        print(d.delete_last())

    d = ArrayDeque()

    for i in range(20):
        d.add_last(i)

    print(d._data)
    while not d.is_empty():
        print(d.delete_first())
