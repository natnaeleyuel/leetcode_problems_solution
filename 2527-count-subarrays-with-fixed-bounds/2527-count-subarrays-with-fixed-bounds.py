class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        n = len(nums)
        lastmink = -1
        lastmaxk = -1
        bound = -1
        for right in range(n):
            curr = nums[right]
            if curr < minK or curr > maxK:
                bound = right
            if curr == minK:
                lastmink = right
            if curr == maxK:
                lastmaxk = right
            
            if lastmink != -1 and lastmaxk != -1:
                m = min(lastmink, lastmaxk)
                result += max(0, m - bound)
        return result