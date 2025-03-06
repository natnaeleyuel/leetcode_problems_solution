class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        range_include = t - 3000
        self.stack.insert(0, t)
        while self.stack and self.stack[-1] < range_include:
            self.stack.pop()
        return len(self.stack)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)