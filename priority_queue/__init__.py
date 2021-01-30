from linked_list.position_list import PositionList
from priority_queue.heap_priority_queue import HeadPriorityQueue


def pq_sort(l: PositionList):
    """Sort a collection of element stored in a positional list."""
    n = len(l)
    p = HeadPriorityQueue()

    for j in range(n):
        element = l.delete(l.first())
        p.add(element, element)

    while not p.is_empty():
        k, v = p.remove_min()
        l.add_last(v)


if __name__ == '__main__':
    import random

    c = PositionList()
    for i in range(20):
        c.add_last(random.randint(0, 20))
    pq_sort(c)
    while not c.is_empty():
        print(c.delete(c.last()))
