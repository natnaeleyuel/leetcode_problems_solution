class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0]) if rows > 0 else 0
        for r in range(rows):
            for c in range(cols):
                left = self.matrix[r][c-1] if c > 0 else 0
                up = self.matrix[r-1][c] if r > 0 else 0
                diag = self.matrix[r-1][c-1] if r > 0 and c > 0 else 0
                self.matrix[r][c] += left + up - diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.matrix[row2][col2]
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        up = self.matrix[row1-1][col2] if row1 > 0 else 0
        diag = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return result - up - left + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)