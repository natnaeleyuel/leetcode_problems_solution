class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = max(candies)
        result = 0
        while low <= high:
            mid = (low + high) // 2
            count = sum(cand // mid for cand in candies)
            if count >= k:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result 
