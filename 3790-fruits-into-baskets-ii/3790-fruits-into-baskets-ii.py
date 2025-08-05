class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        s = set()
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j] and j not in s:
                    s.add(j)
                    break
        return n - len(s)
