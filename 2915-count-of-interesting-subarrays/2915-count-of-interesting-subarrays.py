class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = Counter([0])
        result = 0
        ps = 0
        for i in range(n):
            ps += 1 if nums[i] % modulo == k else 0
            result += count[(ps - k + modulo) % modulo]
            count[ps % modulo] += 1
        
        return result