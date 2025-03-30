class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endind = defaultdict(int)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in endind:
                endind[s[i]] = i
            
        result = []
        maxInd = endind[s[0]]
        for i in range(len(s)):
            maxInd = max(maxInd, endind[s[i]])
            if maxInd == i:
                result.append(i + 1 - sum(result))
            
        return result


