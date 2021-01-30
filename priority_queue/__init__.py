from linked_list.position_list import PositionList
from priority_queue.heap_priority_queue import HeadPriorityQueue


class Wrapper:
    """A Wrapper"""

    def __init__(self, data, f):
        self._f = f
        self.data = data

    def __lt__(self, other):
        return self._f(self.data, other.data)


def pq_sort(coll: PositionList, f=lambda x, y: x < y):
    """Sort a collection of element stored in a positional list."""
    n = len(coll)
    p = HeadPriorityQueue()

    for j in range(n):
        element = coll.delete(coll.first())
        p.add(Wrapper(element, f), element)

    while not p.is_empty():
        k, v = p.remove_min()
        coll.add_last(v)


def heap_sort(coll: list):
    """heap sort without another data."""
    build_heap(coll)
    for index in range(len(coll) - 1, -1, -1):
        coll[index], coll[0] = coll[0], coll[index]
        _heapfiy(coll, index, 0)


def build_heap(coll: list):
    for index in range(len(coll) - 1, -1, -1):
        _heapfiy(coll, len(coll), index)


def _heapfiy(coll: list, length, index):
    """build a heap"""

    if index > length:
        return

    child1 = index * 2 + 1
    child2 = index * 2 + 2

    m = index
    if child1 < length and coll[child1] > coll[m]:
        m = child1

    if child2 < length and coll[child2] > coll[m]:
        m = child2

    if m != index:
        coll[index], coll[m] = coll[m], coll[index]
        _heapfiy(coll, length, m)


if __name__ == '__main__':
    import random

    c = PositionList()
    for i in range(20):
        c.add_last(str(random.randint(0, 20)))
    pq_sort(c, lambda x, y: int(x) < int(y))
    while not c.is_empty():
        print(c.delete(c.last()))

    test_list = [random.randint(0, 20) for i in range(20)]
    heap_sort(test_list)
    print(test_list)
