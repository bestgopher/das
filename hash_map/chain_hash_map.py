from hash_map.hash_map_base import HashMapBase
from hash_map.unsorted_table_map import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(key))
        return bucket[key]

    def _bucket_setitem(self, j, key, value):
        if self._table(j) is None:
            self._table[j] = UnsortedTableMap()

        old_size = len(self._table[j])
        self._table[j][key] = value

        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(key))

        del bucket[key]

    def __iter__(self):
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key
