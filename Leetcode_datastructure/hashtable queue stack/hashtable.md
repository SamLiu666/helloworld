# Hash Table `

Hash Table` is a data structure which organizes data using `hash functions` in order to support quick insertion and search.

There are two different kinds of hash tables: hash set and hash map.

- The `hash set` is one of the implementations of a `set` data structure to store `no repeated values`.
- The `hash map` is one of the implementations of a `map` data structure to store `(key, value)` pairs.

The key idea of Hash Table is to use a hash function to `map keys to buckets`. To be more specific,

1. When we insert a new key, the hash function will decide which bucket the key should be assigned and the key will be stored in the corresponding bucket;
2. When we want to search for a key, the hash table will use the `same` hash function to find the corresponding bucket and search only in the specific bucket.

# Queue & Stack

FIFO  LILO