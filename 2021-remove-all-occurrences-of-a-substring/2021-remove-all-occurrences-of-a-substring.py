class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            arrStr = ['']*len(s)
            ind = s.index(part)
            for i in range(len(s)):
                if i < ind or i > ind + len(part) - 1:
                    arrStr[i] = s[i]
            
            s = ''.join(arrStr)
        
        return s

