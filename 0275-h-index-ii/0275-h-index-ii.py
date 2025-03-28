class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)
        result = 0
        while low < high:
            mid = low + (high - low) // 2
            if citations[mid] >= len(citations) - mid:
                result = mid
                high = mid 
            else:
                low = mid + 1
        if result == 0 and citations[0] == 0:
            return 0
        return len(citations[result:])