class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        b = val not in self.vals
        if b:
            self.vals.append(val)
        
        return b

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """        
        b = val in self.vals
        if b:
            self.vals.remove(val)
        
        return b
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())
