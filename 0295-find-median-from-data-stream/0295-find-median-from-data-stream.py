class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heappush(self.minheap, -num)
        heappush(self.maxheap, -self.minheap[0])
        heappop(self.minheap)

        n1 = len(self.minheap)
        n2 = len(self.maxheap)
        if n1 < n2:
            heappush(self.minheap, -self.maxheap[0])
            heappop(self.maxheap)

    def findMedian(self) -> float:
        n1 = len(self.minheap)
        n2 = len(self.maxheap)

        if n1 > n2:
            return -self.minheap[0]
        else:
            return (self.maxheap[0] - self.minheap[0]) / 2