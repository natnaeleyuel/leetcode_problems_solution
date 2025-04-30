class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        heap = []
        for i in range(n):
            curr_heap = []
            for j in range(m):
                heappush(curr_heap, grid[i][j])
                if len(curr_heap) > limits[i]:
                    heappop(curr_heap)
            
            for ele in curr_heap:
                heappush(heap, ele)
                if len(heap) > k:
                    heappop(heap)
        
        return sum(heap)
