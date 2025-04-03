class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            curr = nums[i] - 1
            if nums[i] != nums[curr]:
                nums[i], nums[curr] = nums[curr], nums[i]
            else:
                i += 1
        
        result = []
        
        for i in range(n):
            if i + 1 != nums[i]:
                result.append(i + 1)
        
        return result