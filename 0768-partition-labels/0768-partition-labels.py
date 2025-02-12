class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counterChr = defaultdict(int)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in counterChr:
                counterChr[s[i]] = i
            
        result = []
        maxInd = counterChr[s[0]]
        for i in range(len(s)):
            maxInd = max(maxInd, counterChr[s[i]])
            if maxInd == i:
                result.append(i + 1 - sum(result))
            
        return result


