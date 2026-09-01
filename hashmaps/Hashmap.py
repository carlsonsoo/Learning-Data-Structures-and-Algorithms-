class HashMap:
    def __init__(self, capacity):
        # number of buckets
        self.capacity = capacity
        # number of elements in the hashmap
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # Adding Methods

    # 1. Length
    def __len__(self):
        return self.size

    # 2. Check if an item is part of the hashmap
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False
    
    # 3. Putting in a new key-value pair
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break

        else:
            bucket.append((key, value))
            self.size += 1

    # 4. Obtain the value of a provided key
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v

        else:
            raise KeyError("Key not found")

    # 5. Remove a key 
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
                
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    # 6. Dictionary methods
    # 6.1 keys
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # 6.2 values
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # 6.3 key-value pairs
    def items(self):
        return [(k,v) for bucket in self.buckets for k, v in bucket]

    # Hash Function - helper function
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for character in key_string:
            # Converting character to ASCII value
            hash_result = (hash_result * 31 + ord(character)) % self.capacity

        return hash_result
    
if __name__ == '__main__':
    hash_map = HashMap(32)
    hash_map.put("name", "Mike")
    hash_map.put("age", 30)
    hash_map.put("job", "Programmer")

    print(hash_map.items())
