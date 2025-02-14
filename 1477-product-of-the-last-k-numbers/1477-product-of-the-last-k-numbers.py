from math import prod
class ProductOfNumbers:

    def __init__(self):
        self.container = []

    def add(self, num: int) -> None:
        self.container.append(num)

    def getProduct(self, k: int) -> int:
        product = prod(self.container[-k:])
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)