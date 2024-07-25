#!/usr/bin/env python3
""" A basic caching system
"""
import base_caching


class BasicCache(base_caching.BaseCaching):
    """ A basic caching system class, it:
      - Overrides the `put` and `get` methods from the BaseCaching class
      - Performing simple adding and accessing data functionalities
    """
    def __init__(self):
        """ Instantiate class object """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache by its key

        Args:
            :param key: item's key
            :param item: value of item

        Returns: None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item data by its key

        Args:
            :param key: item's key

        Returns:
            Item's data or none if the key doesn't exist
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
