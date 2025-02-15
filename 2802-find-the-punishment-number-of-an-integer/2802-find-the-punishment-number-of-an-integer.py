class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_square(s: str, i: int, x: int) -> bool:
            m = len(s)
            if i >= m:
                return x == 0
            y = 0
            for j in range(i, m):
                y = y * 10 + int(s[j])
                if y > x:
                    break
                if is_square(s, j + 1, x - y):
                    return True
            return False

        punishment = 0
        for i in range(1, n+1):
            x = i * i
            if is_square(str(x), 0, i):
                punishment += x
        
        return punishment
            

        