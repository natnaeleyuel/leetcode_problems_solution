class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def recur(ind):
            if ind < len(questions):
                point1 = questions[ind][0] + recur(ind + 1 + questions[ind][1])
                point2 = recur(ind + 1)

                return max(point1, point2)
            return 0
        return recur(0) 
        





