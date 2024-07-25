#!/usr/bin/env python3
""" A caching system, applying the LIFO policy
"""
import base_caching


class LIFOCache(base_caching.BaseCaching):
    """ A caching system implementing the Last In First Out (LIFO) rule
      - Overrides the `put` and `get` methods from the BaseCaching class
        with the principle of LIFO.
      - Enabled restrictions to the number of items stored in the cache to
        MAX_ITEMS defined by class BaseCaching
    """
    last_item = None

    def __init__(self):
        """ Instantiate caching system object """
        super().__init__()

    def put(self, key, item):
        """ Adds or updates an item in the cache by its key.
          - Discards the last item put in cache, when the number of items
            exceeds the MAX_ITEMS defined by the base class (LIFO)
          - Prints the item discarded by its key

          Args:
            :param key: item's key
            :param item: item's value

          Returns: None
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print(f"DISCARD: {self.last_item}")

        self.last_item = key

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
