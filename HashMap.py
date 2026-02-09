# Chaining Method (Linked List) with Polynomial Rolling Hash
class HashNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMaps:
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.buckets = [None] * self.capacity
        self.size = 0
        
    
    # ========== Resizing HashMap ==========
    def resize(self):
        # Store Old Buckets
        old_buckets = self.buckets
        
        # Reset The Map
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        # Old nodes must move to the new Bucket
        for bucket in old_buckets:
            current = bucket
            while current:
                self.set(current.key, current.value)
                current = current.next
    
    # ========== Hash Fucntions ==========
    
    # Polynomial Rolling Hash (base-31)
    def get_hash(self, key):
        hash_val = 0
        for char in str(key):
            hash_val = (hash_val * 31 + ord(char)) % self.capacity
        return hash_val

    # DJB2 Hash (python/C++) 
    def djb2_hash(self, string):
        hash_val = 5381
        for char in str(string):
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        
        return hash_val % self.capacity

    # ========== Handling Collisions with Chaining (Linked List) ==========
    def set(self, key, value):
        # Resize if load factor > 0.7
        if self.size / self.capacity >= 0.7:
            self.resize()
        
        index = self.get_hash(key)
        
        if self.buckets[index] is None:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return
        else:
            
            current = self.buckets[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            current.next = HashNode(key, value)
            self.size += 1
        
    def get(self, key):
        index = self.get_hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise Exception("Key Not Found")
    
    def delete(self, key):
        
        index = self.get_hash(key)
        current = self.buckets[index]
        prev = None
        
        if self.buckets[index] is None:
            raise Exception("Key Not Found")
        else:
            
            if current.next is None:
                current = None
                self.buckets[index] = None
                return True
            else:
                prev = current
                while current:
                    
                    if current.key == key:
                        prev.next = current.next
                        current = None
                        return True
                    
                    prev = current
                    current = current.next
                    
                return current.value
    
    # ========== Utility Fucntions ==========
    
    def contains(self, key):
        for bucket in self.buckets:
            current = bucket
            while current:
                if current.key == key:
                    return True
                current = current.next
        return False
    
    def keys(self):
        
        all_keys = []
        for bucket in self.buckets:
            current = bucket
            while current:
                all_keys.append(current.key)
                current = current.next
        
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.buckets:
            current = bucket
            while current:
                all_values.append(current.value)
                current = current.next
        
        return all_values

