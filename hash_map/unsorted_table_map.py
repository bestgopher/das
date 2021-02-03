from hash_map.map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        """Return value assosiated with key k (raise KeyError if not found)."""

        for item in self._table:
            if k == item._key:
                return item._value

        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, key, value):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if self._table[j]._key == key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(key))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key
