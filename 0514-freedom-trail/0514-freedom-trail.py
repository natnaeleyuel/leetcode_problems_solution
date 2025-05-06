class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def helper(ind, pos, posn, key, ring, memo) -> int:
            if ind == len(key):
                return 0

            if (ind, pos) in memo:
                return memo[(ind, pos)]

            min_steps = float('inf')
            for i in posn[key[ind]]:
                if i >= pos:
                    steps = min(i - pos, pos + len(ring) - i)
                else:
                    steps = min(pos - i, i + len(ring) - pos)
                min_steps = min(min_steps, steps + helper(ind + 1, i, posn, key, ring, memo))
            memo[(ind, pos)] = min_steps + 1
            return min_steps + 1

        memo = {}
        posn = defaultdict(list)
        for i, c in enumerate(ring):
            posn[c].append(i)

        return helper(0, 0, posn, key, ring, memo)
    