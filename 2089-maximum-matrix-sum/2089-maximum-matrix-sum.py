class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_num = float('inf')
        count = 0
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = matrix[i][j]
                if curr < 0:
                    count += 1
                min_num = min(abs(curr), min_num)
                result += abs(curr)
            
        if count % 2:
            result -= min_num * 2
        
        return result