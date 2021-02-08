import random
from hash_map.map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + random.randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = random.randrange(p)  # shift from 0 to p-1 form MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        j = self._hash_function(item)
        return self._bucket_getitem(j, item)

    def __setitem__(self, key, value):
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)

        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0

        for k, v in old:
            self[k] = v

    def _bucket_getitem(self, j, key):
        raise NotImplementedError("implement me")

    def _bucket_setitem(self, j, key, value):
        raise NotImplementedError("implement me")

    def _bucket_delitem(self, j, key):
        raise NotImplementedError("implement me")
