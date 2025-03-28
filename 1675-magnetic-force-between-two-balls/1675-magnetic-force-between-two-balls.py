class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(position, md):
            count = m - 1
            lp = position[0]
            for i in range(1, len(position)):
                curr = position[i] - lp
                if curr >= md:
                    count -= 1
                    lp = position[i]
                    if count == 0:
                        return True
            return count == 0
        
        low = 1
        high = position[-1] - position[0]
        ind = -1
        while low <= high:
            mid = (low + high) // 2
            if check(position, mid):
                ind = mid
                low = mid + 1
            else:
                high = mid - 1
        return ind