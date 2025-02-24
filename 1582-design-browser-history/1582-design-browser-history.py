class BrowserHistory:

    def __init__(self, homepage: str):
        self.bh = []
        self.fh = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.bh.append(url)
        self.fh.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.bh) > 1:
            self.fh.append(self.bh.pop())
            steps -= 1
        return self.bh[-1]        

    def forward(self, steps: int) -> str:
        while steps and self.fh:
            self.bh.append(self.fh.pop())
            steps -= 1
        return self.bh[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)