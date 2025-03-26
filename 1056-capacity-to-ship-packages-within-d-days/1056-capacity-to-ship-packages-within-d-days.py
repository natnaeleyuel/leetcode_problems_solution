class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shipweghts(c):
            count = 0
            tot = 0
            for w in weights:
                curr = tot + w
                if curr > c:
                    tot = w
                    count += 1
                elif curr == c:
                    tot = 0
                    count += 1
                else:
                    tot += w
            
            if tot:
                count += 1
            
            return count <= days
        
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (right + left) // 2 
            if shipweghts(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
