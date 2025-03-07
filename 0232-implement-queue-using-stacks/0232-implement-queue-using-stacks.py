class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            poped = self.stack.pop()
            self.size -= 1
            return poped

    def peek(self) -> int:
        if not self.empty():
            return self.stack[-1]

    def empty(self) -> bool:
        if self.size > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()