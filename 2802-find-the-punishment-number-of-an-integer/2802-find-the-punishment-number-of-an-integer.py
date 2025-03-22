class Solution:
    def punishmentNumber(self, n: int) -> int:
        def recur(s, i, x):
            m = len(s)
            if i >= m:
                return x == 0
            y = 0
            for j in range(i, m):
                y = y * 10 + int(s[j])
                if y > x:
                    break
                if recur(s, j + 1, x - y):
                    return True
            return False

        pun = 0
        for i in range(1, n+1):
            x = i * i
            if recur(str(x), 0, i):
                pun += x
        
        return pun
            

        