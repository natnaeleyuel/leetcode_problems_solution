class NumberContainers:
    def __init__(self):
        self.indexMap = {}
        self.numberMap = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.indexMap:
            prevNumber = self.indexMap[index]
            self.numberMap[prevNumber].remove(index)
        self.indexMap[index] = number
        self.numberMap[number].add(index)

    def find(self, number: int) -> int:
        indices = self.numberMap[number]
        return indices[0] if indices else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)