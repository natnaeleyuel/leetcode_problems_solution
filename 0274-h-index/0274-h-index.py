class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0
        n = len(citations)
        for i in range(n):
            citCorrect = 0
            for j in range(i, n):
                if citations[j] >= n - i:
                    citCorrect += 1
            
            if citCorrect >= n - i:
                res = max(res, n - i)
        
        return res