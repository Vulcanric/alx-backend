#!/usr/bin/env python3
""" A caching system, implementing the LFU algorithm. Also implement a
little of the LRU algorithm for support.
"""
import base_caching
from collections import defaultdict


class LFUCache(base_caching.BaseCaching):
    """ A caching system implementing the Least Frequently Used (LFU) rule.
      - Overrides the `put` and `get` methods from the BaseCaching class
        with the principle of LFU.
      - Enabled restrictions to the number of items stored in the cache to
        MAX_ITEMS defined by class BaseCaching.
    """
    # Counts how frequently each item was accessed
    # LFU algorithm
    count_access = defaultdict(int)

    # For support track how recently an item was accessed
    # LRU algorithm
    track_access = {}  # ex: {'A': least, 'B': recent, 'C': most recent}
    time = 1

    def __init__(self):
        """ Instantiate caching system object """
        super().__init__()

    def put(self, key, item):
        """ Adds or updates an item in the cache by its key.
          - Discards the least-frequently-used item put in cache, when the
            number of items exceeds the MAX_ITEMS defined by the base
            class (LFU)
          - Prints the item discarded by its key

          Args:
            :param key: item's key
            :param item: item's value

          Returns: None
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                fkeys = list(self.count_access.keys())
                lfu = fkeys[0]

                # find the least frequently used item
                for k in fkeys:
                    if self.count_access[lfu] > self.count_access[k]:
                        lfu = k  # lfu = least frequently used

                # lfu is found.
                # If there are more than one lfu's (same frequency)
                # discard the least recently used instead (LRU)
                frequencies = list(self.count_access.values())
                if frequencies.count(self.count_access[lfu]) > 1:
                    rkeys = list(self.track_access.keys())
                    lru = rkeys[0]

                    for k in rkeys:
                        if self.track_access[lru] > self.track_access[k]:
                            lru = k  # lru = least recently used

                        # lru is found, discard it
                        lfu = lru

                # Discard lfu
                self.track_access.pop(lfu)
                self.count_access.pop(lfu)
                self.cache_data.pop(lfu)
                print(f"DISCARD: {lfu}")

            # Item is either updated or inserted (accessed), count frequency!
            self.count_access[key] += 1

            # Also track how recently used
            self.track_access[key] = self.time
            self.time += 1

    def get(self, key):
        """ Retrieves an item from cache by its key.

        Args:
            :param key: Item's key

        Returns:
            Item's value or none if key doesn't exist
        """
        if key in self.cache_data.keys():
            # Item is accessed, count frequency!
            self.count_access[key] += 1

            # Also track how recently used
            self.track_access[key] = self.time
            self.time += 1
            return self.cache_data.get(key)
        return None
