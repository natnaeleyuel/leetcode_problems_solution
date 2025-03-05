class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.count += 1
        else:
            self.count = 0
        
        return self.count >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)