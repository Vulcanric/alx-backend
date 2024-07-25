#!/usr/bin/env python3
""" A caching system, implementing the MRU policy
"""
import base_caching


class MRUCache(base_caching.BaseCaching):
    """ A caching system implementing the Most Recently Used (MRU) rule.
      - Overrides the `put` and `get` methods from the BaseCaching class
        with the principle of MRU.
      - Enabled restrictions to the number of items stored in the cache to
        MAX_ITEMS defined by class BaseCaching.
    """
    # Track the time (order) in which data was accessed
    track_access = {}  # ex: {'A': least, 'B': recent, 'C': most recent}
    time = 1

    def __init__(self):
        """ Instantiate caching system object """
        super().__init__()

    def put(self, key, item):
        """ Adds or updates an item in the cache by its key.
          - Discards the most recently used item put in cache, when the
            number of items exceeds the MAX_ITEMS defined by the base
            class (MRU)
          - Prints the item discarded by its key

          Args:
            :param key: item's key
            :param item: item's value

          Returns: None
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                keys = list(self.track_access.keys())
                mru = keys[0]

                # Find the data with the most recent time/order
                for k in keys:
                    if self.track_access[mru] < self.track_access[k]:
                        mru = k  # mru = most recent

                # mru is found! Uncomment the next line to see process flow
                # print(self.track_access, mru, 'is the most recently used')
                self.cache_data.pop(mru)
                self.track_access.pop(mru)
                print(f"DISCARD: {mru}")

            # Item is updated or inserted (accessed), track time!
            self.track_access[key] = self.time
            self.time += 1

    def get(self, key):
        """ Retrieves an item from cache by its key.

        Args:
            :param key: Item's key

        Returns:
            Item's value or none if key doesn't exist
        """
        # Item is accessed, track time!
        if key in self.cache_data.keys():
            self.track_access[key] = self.time
            self.time += 1
            return self.cache_data.get(key)
        return None
