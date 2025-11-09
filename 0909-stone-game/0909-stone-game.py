class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            check = True if (r - l) % 2 else False
            lft = piles[l] if check else 0
            rgt = piles[r] if check else 0

            dp[(l, r)] = max(
                dfs(l + 1, r) + lft,
                dfs(l, r - 1) + rgt
            )

            return dp[(l, r)]
        
        return dfs(0, n - 1) > sum(piles) // 2