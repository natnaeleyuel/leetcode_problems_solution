class Solution:
    MOD = 10**9 + 7
    def numSub(self, s: str) -> int:
        n = len(s)
        res = 0
        consec = 0
        for i in range(n):
            if s[i] == "0":
                consec = 0
            else:
                consec += 1
                res = (res + consec) % self.MOD 
                
        return res