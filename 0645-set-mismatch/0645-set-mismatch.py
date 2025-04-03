class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        result = []
        while i < n:
            curr = nums[i] - 1
            if nums[i] != nums[curr]:
                nums[i], nums[curr] = nums[curr], nums[i]
            else:
                if i != curr and len(result) == 0:
                    result.append(nums[i])
                i += 1
                
        for i in range(n):
            if i + 1 != nums[i]:
                result.append(i+1)
        
        return result