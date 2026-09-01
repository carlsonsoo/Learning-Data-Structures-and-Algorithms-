class HashMap:
    def __innit__(self, capacity):
        # number of buckets
        self.capacity = capacity
        # number of elements in the hashmap
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # Adding Methods

    # 1. Length
    def __len__(self):
        pass

    # 2. Check if an item is part of the hashmap
    def __contains__(self, key):
        pass

    # 3. Putting in a new key-value pair
    def put(self, key, value):
        pass

    # 4. Obtain the value of a provided key
    def get(self, key):
        pass

    # 5. Remove a key 
    def remove(self, key):
        pass

    # 6. Dictionary methods
    # 6.1 keys
    def keys(self):
        pass

    # 6.2 values
    def values(self):
        pass

    # 6.3 key-value pairs
    def items(self):
        pass

    # Hash Function - helper function
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for character in key_string():
            # Converting character to ASCII value
            hash_result = (hash_result * 31 + ord(character)) % self.capacity

