from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        pass

        self.collision_type=collision_type
        self.params=params
        if collision_type == "Chain":
            self.table_size = params[1]
            self.table = [None]*self.table_size
        elif collision_type == "Linear":
            self.table_size = params[1]
            self.table = [None] * self.table_size
        else:  # Double hashing
            self.table_size = params[3]
            self.table = [None] * self.table_size
        
    def first_hash_function(self, key , z, Mod):
        hash_value=0
        k=1
        for x in key:
            hash_value=(hash_value + self.latin_assigning(x)*k)%Mod
            k=(k*z)%Mod
        return hash_value%Mod
    
    def latin_assigning(self, letter):
        if letter.isupper():
            return ord(letter) - ord('A')+26
        else:
            return ord(letter) - ord('a')
        
    def second_hash_function(self, key, z2, c2):
        hash_value=0
        k=1
        for x in key:
            hash_value=(hash_value + self.latin_assigning(x)*k)%c2
            k=(k*z2)%c2
        return c2-(hash_value%c2)
    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        pass
    
    def __str__(self):
        if self.collision_type == "Chain":
            return self._format_chain()
        else:
            return self._format_linear()

    def _format_chain(self):
        slots = []
        for slot in self.table:
            if not slot:
                slots.append("<EMPTY>")
            else:
                slot_values = []
                for item in slot:
                    if isinstance(item, tuple):
                        slot_values.append(f"({item[0]},{item[1]})")
                    else:
                        slot_values.append(str(item))
                slots.append(" ; ".join(slot_values))
        return " | ".join(slots)

    def _format_linear(self):
        slots = []
        for slot in self.table:
            if slot is None:
                slots.append("<EMPTY>")
            elif isinstance(slot, tuple):
                slots.append(f"({slot[0]},{slot[1]})")
            else:
                slots.append(str(slot))
        return " | ".join(slots)
            
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        self.total_elements=0
        pass
    
    def insert(self, key):
        hash_value = self.first_hash_function(key, self.params[0], self.table_size)
        if self.collision_type == "Chain":
            self._insert_chain(hash_value, key)
        elif self.collision_type == "Linear":
            self._insert_linear(hash_value, key)
        else:
            self._insert_quadratic(hash_value, key)

    def _insert_chain(self, hash_value, key):
        current = self.table[hash_value]
        if current is None:
            self.table[hash_value] = [key]
            self.total_elements += 1
        else:
            if key not in current:
                current.append(key)
                self.total_elements += 1
            self.table[hash_value] = current

    def _insert_linear(self, hash_value, key):
        index = hash_value
        while True:
            if self.table[index] is None or self.table[index] == key:
                if self.table[index] is None:
                    self.table[index] = key
                    self.total_elements += 1
                return
            else:
                index = (index + 1) % self.table_size
            if index == hash_value:
                return

    def _insert_quadratic(self, hash_value, key):
        index = hash_value
        gap = self.second_hash_function(key, self.params[1], self.params[2])
        while True:
            if self.table[index] is None or self.table[index] == key:
                if self.table[index] is None:
                    self.table[index] = key
                    self.total_elements += 1
                return
            else:
                index = (index + gap) % self.table_size
            if index == hash_value:
                return
    
    def find(self, key):
        hash_value = self.first_hash_function(key, self.params[0], self.table_size)
        if self.collision_type == "Chain":
            return self._find_in_chain(hash_value, key)
        elif self.collision_type == "Linear":
            return self._find_in_linear(hash_value, key)
        else:
            return self._find_in_quadratic(hash_value, key)

    def _find_in_chain(self, hash_value, key):
        current = self.table[hash_value]
        if current is None:
            return False
        for x in current:
            if x == key:
                return True
        return False

    def _find_in_linear(self, hash_value, key):
        index = hash_value
        while True:
            if self.table[index] is None:
                return False
            elif self.table[index] == key:
                return True
            else:
                index = (index + 1) % self.table_size
            if index == hash_value:
                return False

    def _find_in_quadratic(self, hash_value, key):
        index = hash_value
        gap = self.second_hash_function(key, self.params[1], self.params[2])
        while True:
            if self.table[index] is None:
                return False
            elif self.table[index] == key:
                return True
            else:
                index = (index + gap) % self.table_size
            if index == hash_value:
                return False
    
    def get_load(self):
        return self.total_elements/self.table_size
    
    def get_slot(self, key):
        return self.first_hash_function(key, self.params[0], self.table_size)
    
    def __str__(self):
        return super().__str__()
    
    def items(self):
        keys = []
        if self.collision_type == "Chain":
            for slot in self.table:
                if slot:
                    keys.extend(slot)
        else:
            for slot in self.table:
                if slot is not None:
                    keys.append(slot)
        return keys
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        self.total_elements=0
        pass
    
    def insert(self, x):
        # x = (key, value)
        key = x[0]
        hash_value = self.first_hash_function(key, self.params[0], self.table_size)

        if self.collision_type == "Chain":
            self._insert_chain(hash_value, x, key)
        elif self.collision_type == "Linear":
            self._insert_linear(hash_value, x, key)
        else:  # Assuming the only other option is "Quadratic"
            self._insert_quadratic(hash_value, x, key)

    def _insert_chain(self, hash_value, x, key):
        if self.table[hash_value] is None:
            self.table[hash_value] = [x]
            self.total_elements += 1
        else:
            if not any(item[0] == key for item in self.table[hash_value]):
                self.table[hash_value].append(x)
                self.total_elements += 1

    def _insert_linear(self, hash_value, x, key):
        index = hash_value
        while True:
            current_item = self.table[index]
            if current_item is None:
                self.table[index] = x
                self.total_elements += 1
                return
            elif current_item[0] == key:
                return  # Key already exists; do nothing
            index = (index + 1) % self.table_size
            if index == hash_value:
                return  # Table is full

    def _insert_quadratic(self, hash_value, x, key):
        index = hash_value
        gap = self.second_hash_function(key, self.params[1], self.params[2])
        while True:
            current_item = self.table[index]
            if current_item is None:
                self.table[index] = x
                self.total_elements += 1
                return
            elif current_item[0] == key:
                return  # Key already exists; do nothing
            index = (index + gap) % self.table_size
            if index == hash_value:
                return  # Table is full

    
    def find(self, key):
        hash_value = self.first_hash_function(key, self.params[0], self.table_size)

        if self.collision_type == "Chain":
            return self._find_chain(hash_value, key)
        elif self.collision_type == "Linear":
            return self._find_linear(hash_value, key)
        else:  # Assuming the only other option is "Double"
            return self._find_double(hash_value, key)

    def _find_chain(self, hash_value, key):
        bucket = self.table[hash_value]
        if bucket is None:
            return None
        
        for item in bucket:
            if item[0] == key:
                return item[1]
        
        return None

    def _find_linear(self, hash_value, key):
        index = hash_value
        while True:
            current_item = self.table[index]
            if current_item is None:
                return None
            if current_item[0] == key:
                return current_item[1]
            
            index = (index + 1) % self.table_size
            if index == hash_value:
                return None

    def _find_double(self, hash_value, key):
        index = hash_value
        gap = self.second_hash_function(key, self.params[1], self.params[2])
        
        while True:
            current_item = self.table[index]
            if current_item is None:
                return None
            if current_item[0] == key:
                return current_item[1]
            
            index = (index + gap) % self.table_size
            if index == hash_value:
                return None
            
    def get_load(self):
        return self.total_elements/self.table_size
    
    def get_slot(self, key):
        return self.first_hash_function(key, self.params[0], self.table_size)
    
    def __str__(self):
        return super().__str__()
        pass

