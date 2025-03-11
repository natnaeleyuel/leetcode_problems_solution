class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        init1 = [1]
        init2 = [1, 1]
        if rowIndex == 0:
            return init1
        elif rowIndex == 1:
            return init2
        k = 1
        while k < rowIndex:
            init1 = init2
            init2 = [1] * (len(init1) + 1)
            l = 1
            while l < len(init2) - 1:
                init2[l] = init1[l-1] + init1[l]
                l += 1
            k += 1
        return init2

