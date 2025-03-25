class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check_cuts(rectangles, dimension):
            gap_count = 0
            rectangles.sort(key= lambda rectangle: rectangle[dimension])
            furthest_end = rectangles[0][dimension + 2]

            for i in range(1, len(rectangles)):
                if furthest_end <= rectangles[i][dimension]:
                    gap_count += 1
                
                furthest_end = max(furthest_end, rectangles[i][dimension + 2])
            
            return gap_count >= 2
        
        return check_cuts(rectangles, 0) or check_cuts(rectangles, 1)
