class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        rec = self.countAndSay(n-1)
        result = ""
        k = 0
        s = ""
        for i in rec:
            if i == s:
                k += 1
            elif k != 0:
                result += str(k) + s
                k = 1
                s = i
            else:
                k = 1
                s = i
        result += str(k) + s
        return result 