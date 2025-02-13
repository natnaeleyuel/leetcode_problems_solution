class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        result = 0
        while len(nums) > 1 and nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            result += 1
        return result