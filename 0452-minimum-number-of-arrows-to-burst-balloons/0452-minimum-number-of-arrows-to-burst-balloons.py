class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key= lambda p: p[1])
        res = 1
        curr = []
        for i in range(1, len(points)):
            if i == 1:
                if points[i][0] <= points[i-1][1]:   
                    curr = [points[1][0], min(points[0][1], points[1][1])]
                else:
                    curr = points[1]
                    res += 1

            else:
                if points[i][0] <= curr[1]:
                    curr = [points[i][0], min(curr[1], points[i][1])]
                else:
                    curr = points[i]
                    res += 1
           
        return res
        

