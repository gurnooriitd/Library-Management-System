from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        new_table = [None] * new_size
        
        old_table = self.table.copy()
        self.table = new_table
        self.table_size = new_size
        self.total_elements = 0  # Reset element count as we will re-insert
        
        for slot in old_table:
            if slot is not None:
                if self.collision_type == "Chain":
                    for element in slot:  # Rehash each element in the chain
                        self.insert(element)
                else:
                    self.insert(slot)  # Rehash single element in probing
        pass
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        new_table = [None] * new_size
        
        old_table = self.table
        self.table = new_table
        self.table_size = new_size
        self.num_elements = 0  # Reset element count as we will re-insert
        
        for slot in old_table:
            if slot is not None:
                if self.collision_type == "Chain":
                    for element in slot:  # Rehash each element in the chain
                        self.insert(element)
                else:
                    self.insert(slot)  # Rehash single element in probing
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()