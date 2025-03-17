class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i 
        return len(citations)
