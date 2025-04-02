class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s_set = set()
        n = len(nums)
        for i in range(n):
            if nums[i] not in s_set:
                s_set.add(nums[i])
            else:
                s_set.remove(nums[i])
            
        return list(set(nums).difference(s_set))
