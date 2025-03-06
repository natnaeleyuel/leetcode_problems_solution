class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n ** 2
        repeated = 0
        presum = 0
        freq = [0] * (size + 1)

        for row in grid:
            for num in row:
                freq[num] += 1
                if freq[num] == 2:
                    repeated = num
                presum += num

        presum -= repeated
        totsum = size * (size + 1) // 2
        missed = totsum - presum

        return [repeated, missed]


