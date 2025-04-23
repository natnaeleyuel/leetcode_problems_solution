class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for num in range(1, n + 1):
            tot = 0
            k = num
            while k != 0:
                tot += k % 10
                k = k // 10
            d[tot] += 1
        
        max_val = max(d.values())
        count = Counter(d.values())
        return count[max_val]
