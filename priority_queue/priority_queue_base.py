class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store prority queue items."""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Return the length."""
        NotImplementedError("implement it")
