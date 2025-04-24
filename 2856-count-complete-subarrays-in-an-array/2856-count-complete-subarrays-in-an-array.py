class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dist = len(set(nums))
        result = 0

        for i in range(n):
            curr_set = set()
            for j in range(i, n):
                curr_set.add(nums[j])
                if len(curr_set) == dist:
                    result += n - j
                    break
        
        return result