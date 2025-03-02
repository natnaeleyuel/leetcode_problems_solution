class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            if d[nums[i]] < 2:
                d[nums[i]] += 1
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            
        return left