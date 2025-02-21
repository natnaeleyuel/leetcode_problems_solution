class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0]*1001
        for pas, fro, to in trips:
            prefix_sum[fro] += pas
            prefix_sum[to] -= pas
        
        result = all(t <= capacity for t in accumulate(prefix_sum))
        return result