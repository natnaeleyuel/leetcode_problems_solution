class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = int(math.sqrt(n))
        sec = (n + m - 1) // m
        count = 0
        max_values = [0] * sec
        for i in range(n):
            max_values[i // m] = max(max_values[i // m], baskets[i])
        for fruit in fruits:
            k = 1
            for s in range(sec):
                if max_values[s] < fruit:
                    continue
                cond = False
                max_values[s] = 0
                for i in range(m):
                    p = s * m + i
                    if p < n and baskets[p] >= fruit and not cond:
                        baskets[p] = 0
                        cond = True
                    if p < n:
                        max_values[s] = max(max_values[s], baskets[p])
                k = 0
                break
            count += k
        return count
