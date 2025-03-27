class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(m):
            day_count = 0
            total = 0

            for weight in weights:
                total += weight
                if total > m:
                    day_count += 1
                    total = weight
                if day_count == days:
                    return False
            return True
        
        high = sum(weights)
        low = max(weights)
        while low <= high:
            mid = (high + low) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low