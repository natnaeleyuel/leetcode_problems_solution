class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.total = sum(self.arr)

    def sumRange(self, left: int, right: int) -> int:
        result = self.total
        for i in range(left):
            result -= self.arr[i]
        for j in range(right+1, len(self.arr)):
            result -= self.arr[j]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)