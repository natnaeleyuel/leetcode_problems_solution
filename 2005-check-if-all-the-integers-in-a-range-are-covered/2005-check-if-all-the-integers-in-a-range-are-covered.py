class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        minNum = float('inf')
        maxNum = -float('inf')
        for i in range(len(ranges)):
            minNum = min(minNum, ranges[i][0])
            maxNum = max(maxNum, ranges[i][1])

        if left < minNum or left > maxNum:
            return False

        elif right < minNum or right > maxNum:
            return False
        
        else:
            count = 0
            for num in range(left, right + 1):
                for j in range(len(ranges)):
                    if num >= ranges[j][0] and num <= ranges[j][1]:
                        count += 1
                        break
            
            return count == right - left + 1

                    
        