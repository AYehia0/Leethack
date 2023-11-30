from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        # storing the data in O(1)
        self.store = []
        
        # stores the index of the element to be added for removing in O(1)
        self.index_store = {}

    def insert(self, val: int) -> bool:
        if val in self.index_store:
            return False
        
        self.index_store[val] = len(self.store)
        self.store.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_store:
            return False
        
        remove_ind = self.index_store[val]
        last = self.store[-1]
        
        # Update the index_store for the last element
        self.index_store[last] = remove_ind
        
        # Move the last value to that index and then pop from the array
        self.store[remove_ind] = last
        self.store.pop()

        # Remove the entry for the removed element from index_store
        del self.index_store[val]

        return True
    
    def getRandom(self) -> int:
        random_ind = random.randint(0, len(self.store) - 1)
        return self.store[random_ind]
