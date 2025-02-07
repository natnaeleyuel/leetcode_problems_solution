class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorMap = {}
        colorCount = Counter()
        result = []
          
        for ball, color in queries:
            colorCount[color] += 1
            if ball in colorMap:
                colorCount[colorMap[ball]] -= 1
                if colorCount[colorMap[ball]] == 0:
                    colorCount.pop(colorMap[ball])
            colorMap[ball] = color
            result.append(len(colorCount))
        
        return result
