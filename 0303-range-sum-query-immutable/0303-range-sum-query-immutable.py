class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        for i in range(1, len(self.arr)):
            self.arr[i] = self.arr[i] + self.arr[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        return self.arr[right] - self.arr[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)