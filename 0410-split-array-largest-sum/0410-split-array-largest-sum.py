class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(m):
            tot = 0
            count = 0
            for num in nums:
                curr = tot + num
                if curr > m:
                    tot = num
                    count += 1
                elif curr == m:
                    tot = 0
                    count += 1
                else:
                    tot += num
                
            if tot:
                count += 1
            
            return count <= k
        
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low