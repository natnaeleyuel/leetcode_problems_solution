class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freedays = 0
        lastend = 0

        for start, end in meetings:
            if start > lastend + 1:
                freedays += start - lastend - 1
            
            lastend = max(lastend, end)
        
        freedays += days - lastend
        return freedays

