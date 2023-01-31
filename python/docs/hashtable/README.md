# Hashtables
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:

- set
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.
- get
    - Arguments: key
    - Returns: Value associated with that key in the table
- has
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
- keys
    - Returns: Collection of keys
- hash
    - Arguments: key
    - Returns: Index in the collection for that key


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available in each of your hashtable -->
- __init__(self): Initializes a new instance of the Hashtable class with an empty table of size 256 (to represent the possible hash values).

- hash(self, key): Hashes the key to an integer within the range [0, 255]. The hashing function used in this example is the built-in hash() function.

- set(self, key, value): Sets the value associated with the given key in the table. If the key already exists, its value will be updated. If there is a collision (two keys hash to the same index), the new key-value pair will be appended to the same index as a tuple.

- get(self, key): Retrieves the value associated with the given key from the table. If the key does not exist, returns None.

- has(self, key): Returns a boolean indicating whether the given key exists in the table.

- keys(self): Returns a list of all unique keys that exist in the table.