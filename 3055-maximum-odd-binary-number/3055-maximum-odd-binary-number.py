class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = list(s)
        l = sorted(l, key= lambda x: int(x))
        k = l.pop()
        l = [k] + l
        return ''.join(l[::-1])