class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        row, count = 0, 0
        for i in range(n):
            k = 0
            for j in range(m):
                if mat[i][j] == 1:
                    k += 1
            if k > count:
                count = k
                row = i
        return [row,count]   