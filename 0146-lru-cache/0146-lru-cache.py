class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lrucache = {}
        
    def get(self, key: int) -> int:
        if key in self.lrucache:
            result = self.lrucache[key]
            del self.lrucache[key]
            self.lrucache[key] = result
            return result
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            del self.lrucache[key]
            self.lrucache[key] = value
        elif len(self.lrucache) == self.capacity:
            for k in self.lrucache:
                old_used = k
                del self.lrucache[old_used]
                self.lrucache[key] = value
                break
        elif len(self.lrucache) < self.capacity:
            self.lrucache[key] = value
             




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)