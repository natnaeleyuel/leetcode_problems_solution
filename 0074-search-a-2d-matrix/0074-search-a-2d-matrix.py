class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        lr = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target:
                lr = mid
                low = mid + 1
            else:
                high = mid - 1
        if lr == -1:
            return False
        
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[lr][mid] == target:
                return True
            elif matrix[lr][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False