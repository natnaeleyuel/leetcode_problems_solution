class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        k, l = len(mat), len(mat[0])
        for ind in range(k + l - 1):
            newArr = []
            i = 0 if ind < l else ind - l + 1
            j = ind if ind < l else l - 1
            while i < k and j >= 0:
                newArr.append(mat[i][j])
                i += 1
                j -= 1
            if ind % 2 == 0:
                newArr = newArr[::-1]
            result.extend(newArr)
        return result