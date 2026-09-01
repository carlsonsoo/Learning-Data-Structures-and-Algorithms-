class HashMap:
    def __innit__(self, capacity):
        # number of buckets
        self.capacity = capacity
        # number of elements in the hashmap
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    