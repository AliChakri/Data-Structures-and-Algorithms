# The Open Addressing (Double Hashing) + DJ2B Hash Method and Hash2 with Prime numbers
class DoubleHashMap:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.DELETED = "!!!TOMBSTONE!!!" # marker for deleted slots
        
    # ========== Resizing HashMap ==========
    def resize(self):
        # Store Old Keys and Values
        old_keys = self.keys
        old_values = self.values
        
        # Reset The Map
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        
        # Old nodes must move to the new Bucket
        for i in range(len(old_keys)):
            key = old_keys[i]
            
            if key is not None and key != self.DELETED:
                self.set(key, old_values[i])
    
    # ========== Hash Fucntions ==========
    
    def dj2b_hash(self, key):
        hash_val = 5381
        for char in str(key):
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        return hash_val % self.capacity
    
    def secondary_hash(self, key):
        """Secondary Hash: Determines the 'jump' size (must never be 0)."""
        # (Prime - (hash % Prime))
        p = 7
        return p - (hash(key) % p)
    
    # ========== Operation Fucntions ==========
    
    def set(self, key, value):
        # Resize if load factor > 0.7
        if self.size / self.capacity >= 0.7:
            self.resize()
        
        index = self.dj2b_hash(key)
        step = self.secondary_hash(key)
        
        # Look for the key, an empty slot (None), or a Tombstone
        first_tombstone = None
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            
            # Optimization: Remember the first tombstone we see to reuse it
            if self.keys[index] == self.DELETED and first_tombstone is None:
                first_tombstone = index
            
            index = (index + step) % self.capacity
        
        # If we found a tombstone and didn't find the key, reuse the tombstone slot
        insertion_index = first_tombstone if first_tombstone is not None else index
        self.keys[insertion_index] = key
        self.values[insertion_index] = value
        self.size += 1
    
    def get(self, key):
        index = self.dj2b_hash(key)
        step = self.secondary_hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            
            index = (index + step) % self.capacity
            
            # If All Cases are Tomb Stone
            if index == start_index:
                break
        return None
    
    def delete(self, key):
        index = self.dj2b_hash(key)
        step = self.secondary_hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = self.DELETED
                self.values[index] = None
                self.size -= 1
                return True
            index = (index + step) % self.capacity
        return False

    # ========== Utilities Fucntion ==========
    def get_keys(self):
        all_keys = []
        for key in self.keys:
            if key is not None and key != self.DELETED:
                all_keys.append(key)
        
        return all_keys
    
    def get_values(self):
        all_values = []
        for val in self.values:
            if val is not None:
                all_values.append(val)
        
        return all_values

    def contains(self, key):
        
        for k in self.keys:
            if k == key:
                return True
        return False
