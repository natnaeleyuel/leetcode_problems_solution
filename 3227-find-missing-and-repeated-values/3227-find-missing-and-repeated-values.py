class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numsdict = defaultdict(int)
        repeated = 0
        presum = 0

        for row in grid:
            for col in row:
                presum += col
                if numsdict[col] > 0:
                    repeated = col
                numsdict[col] += 1

        n = len(grid)
        n = n ** 2
        presum -= repeated
        totsum = n * (n + 1) // 2
        missed = totsum - presum

        return [repeated, missed]


