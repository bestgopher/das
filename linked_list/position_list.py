from linked_list.base import _DoublyLinkedBase
from linked_list._node import _DoubleNode


class Position:
    """A abstraction representing the location of a single element."""

    def __init__(self, container, node: _DoubleNode):
        """Constructor should not be invoked by user."""
        self._container = container
        self._node = node

    def element(self):
        """Return the element stored at this position"""
        return self._node.value

    def __eq__(self, other):
        """Return True if other is a Position representing the same location."""
        return type(self) is type(other) and other.node is self.node

    def __ne__(self, other):
        """Return True if other does not represent the same location."""
        return not (self == other)

    @property
    def node(self):
        return self._node

    @property
    def container(self):
        return self._container


class PositionList(_DoublyLinkedBase):
    """A sequential container of elements allowing position access."""

    def _validate(self, p: Position):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type.")
        if p.container is not self:
            raise ValueError("p does not belong to this container.")

        if p.node.next is None:
            raise ValueError("p is not longer valid.")

        return p.node

    def _make_position(self, node: _DoubleNode):
        """Return Position instance for given node(or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None

        return Position(self, node)

    def first(self):
        """Return the first position in the list(or None if list is empty)."""
        return self._make_position(self._header.next)

    def last(self):
        """Return the last Position in the list(or None if list is empty)."""
        return self._make_position(self._trailer.prev)

    def before(self, p: Position):
        """Return the Position just before Position p(or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p: Position):
        """Return the Position just after Position p(or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Positon."""
        origin = self._validate(p)
        return self._insert_between(e, origin.prev, origin)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Positon."""
        origin = self._validate(p)
        return self._insert_between(e, origin, origin.next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        origin = self._validate(p)
        return self._delete_node(origin)

    def replace(self, p, e):
        """
        Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        origin = self._validate(p)
        old_value = origin.value
        origin.value = e
        return old_value


def insertion_sort(l: PositionList):
    """Sort PositionalList of comparable elements into non-decreasing order."""

    if len(l) == 0:
        return

    marker = l.first()
    while marker != l.last():
        pivot = l.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != l.first() and l.before(walk).element() > value:
                walk = l.before(walk)
            l.delete(pivot)
            l.add_before(walk, value)
