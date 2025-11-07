class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i in range(n):
            left = max(i - r, 0)
            right = min(i + r + 1, n)
            diff[left] += stations[i]
            diff[right] -= stations[i]
        
        def possible(mid):
            curr_p = 0
            curr_k = k
            diff_cpy = diff.copy()
            for i in range(n):
                curr_p += diff_cpy[i]
                if curr_p < mid:
                    additional = mid - curr_p 
                    if additional > curr_k:
                        return False
                    curr_k -= additional 
                    curr_p += additional 
                    right = min(i + 2*r + 1, n)
                    diff_cpy[right] -= additional

            return True
        
        low, high = min(stations), sum(stations) + k
        res = low 
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
            