#!/usr/bin/env python3
""" A caching system, implementing the LRU policy
"""
import base_caching


class LRUCache(base_caching.BaseCaching):
    """ A caching system implementing the Least Recently Used (LRU) rule.
      - Overrides the `put` and `get` methods from the BaseCaching class
        with the principle of LRU.
      - Enabled restrictions to the number of items stored in the cache to
        MAX_ITEMS defined by class BaseCaching.
    """
    # Track the time (order) in which data was accessed
    track_access = {}  # ex: {'A': least, 'B': recent, 'C': most recent}
    time = 0

    def __init__(self):
        """ Instantiate caching system object """
        super().__init__()

    def put(self, key, item):
        """ Adds or updates an item in the cache by its key.
          - Discards the least recently used item put in cache, when the
            number of items exceeds the MAX_ITEMS defined by the base
            class (LRU)
          - Prints the item discarded by its key

          Args:
            :param key: item's key
            :param item: item's value

          Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            self.track_access[key] = self.time
            self.time += 1

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            keys = list(self.track_access.keys())
            lru = keys[0]

            # Find the data with the least time/order
            for key in keys:
                if self.track_access[lru] > self.track_access[key]:
                    lru = key  # lru = least

            # lru is found! Uncomment the next line to see full process flow
            # print(self.track_access, lru, 'is the least recently used')
            self.cache_data.pop(lru)
            self.track_access.pop(lru)
            print(f"DISCARD: {lru}")

    def get(self, key):
        """ Retrieves an item from cache by its key.

        Args:
            :param key: Item's key

        Returns:
            Item's value or none if key doesn't exist
        """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
