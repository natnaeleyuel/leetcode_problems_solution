class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(queens, diff, summ):
            l = len(queens)
            if l == n:
                result.append(queens)
                return None
            
            for i in range(n):
                if i not in queens and l - i not in diff and l + i not in summ:
                    backtrack(queens + [i], diff + [l-i], summ + [l + i])
                
        result = []
        backtrack([], [], [])

        return [ ["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]