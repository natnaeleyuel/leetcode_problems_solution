class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        i = 0
        j = 0
        curr = 0
        for diff in differences:
            curr += diff
            i = min(i, curr)
            j = max(j, curr)
            if j - i > upper - lower:
                return 0
        
        return upper - lower - j + i + 1