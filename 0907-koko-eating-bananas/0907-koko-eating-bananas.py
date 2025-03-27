class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(c):
            hour_count = 0
            for pile in piles:
                hour_count += ceil(pile / c)
                if hour_count > h:
                    return False
            return True
        
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
