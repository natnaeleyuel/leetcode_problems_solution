class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        k = target
        opr = 0
        while k > 1:
            if maxDoubles == 0:
                opr += k - 1
                k = 1
            elif maxDoubles > 0 and k / 2 == k // 2 and k / 2 >= 1:
                opr += 1
                maxDoubles -= 1
                k = k // 2
            elif k - 1 >= 1:
                    opr += 1
                    k -= 1

        return opr
