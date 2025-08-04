class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)
        n = len(fruits)
        for i in range(n):
            fruit_count[fruits[i]] += 1
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_len = max(max_len, i - start + 1)
        return max_len