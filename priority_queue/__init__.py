from linked_list.position_list import PositionList
from priority_queue.heap_priority_queue import HeadPriorityQueue


class Wrapper:
    """A Wrapper"""

    def __init__(self, data, f):
        self._f = f
        self.data = data

    def __lt__(self, other):
        return self._f(self.data, other.data)


def pq_sort(l: PositionList, f=lambda x, y: x < y):
    """Sort a collection of element stored in a positional list."""
    n = len(l)
    p = HeadPriorityQueue()

    for j in range(n):
        element = l.delete(l.first())
        p.add(Wrapper(element, f), element)

    while not p.is_empty():
        k, v = p.remove_min()
        l.add_last(v)


if __name__ == '__main__':
    import random

    c = PositionList()
    for i in range(20):
        c.add_last(str(random.randint(0, 20)))
    pq_sort(c, lambda x, y: int(x) < int(y))
    while not c.is_empty():
        print(c.delete(c.last()))
