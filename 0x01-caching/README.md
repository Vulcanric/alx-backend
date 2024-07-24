# 0x01. Caching
`**Back-end**`

## Description:
In this project, I worked with different Cache replacement policies (a.k.a cache replacement algorithms or just cache algorithms for short), gaining insightful knowledge on these algorithms, their functionalities, use cases and limitations.

## Overview:
### Caching
Caching is the process of storing frequently-used data or resource in a temporary storage area, called a cache, to improve access speed. It is done to reduce the time and resources it takes to retrieve or compute this data from the system's main memory.

### Caching algorithms
Cache replacement policies are a set of rules or technique used by computer programs or hardware-based systems to efficiently manage and update the contents of a cache, ensuring optimal performance and data accessibility.

## Examples of such policies
### 1. FIFO (First In First Out)
- Discards data in the order they were added (queue).
- Doesn't consider how often or recently they were accessed.
### 2. LIFO (Last In First out)
- Discards the most recently added data first.
- Behaves like a stack.
### 3. LRU (Least Recently Used)
- Keeps track of the last time each data was accessed/used.
- Discards the one that has been idle the most.
### 4. MRU (Most Recently Used)
- Discards the most recently used item
- Suitable for situations where the older item is, more likely to be used again.
### 5. LFU (Least Frequently Used)
- Counts the number of times each item was accessed
- Discards the item with the lowest count.

And many other...

## Limitations of a Caching System:
1. Caching size: The amount of memory or storage available for caching is limited.
2. Cache coherence: Ensuring data consistency between caching systems and the main memory.
3. Cache pollution: Unproductive use of the caching system through storing of unecessary data.
And lot more...
