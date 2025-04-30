class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []

        for i in range(n - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return i
        
        return n - 1

                    
