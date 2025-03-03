class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = defaultdict(int)
        result = 0
        for i in range(len(s)):
            curr = s[i]
            d[curr] += 1
            if d['R'] > 0 and d['R'] == d['L']:
                  result += 1
                  d['R'] = 0
                  d['L'] = 0
        return result
