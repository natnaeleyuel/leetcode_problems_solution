class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n=len(nums)
        d = defaultdict(int)
        result = 0
        count = 0 
        left = 0
        for ind, num in enumerate(nums):
            count += d[num]
            d[num] += 1
            while count >= k:
                result += n - ind
                d[nums[left]] -= 1
                count -= d[nums[left]]
                left += 1
        return result