class RandomizedSet:

    def __init__(self):
        self.randomized_set = set()
        self.nums_dict = dict()

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set.add(val)
            self.nums_dict[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            del self.nums_dict[val]
            return True
        return False
        
    def getRandom(self) -> int:
        random_num = random.choice(list(self.nums_dict.keys()))
        return random_num
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()