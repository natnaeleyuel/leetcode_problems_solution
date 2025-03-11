class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(invert):
            res = []
            for i in range(len(invert)):
                if invert[i] == '0':
                    res.append('1')
                else:
                    res.append('0')
            return ''.join(res[::-1])
        def recur_fun(n):
            if n == 1:
                return '0'
            return recur_fun(n-1) + '1' + helper(recur_fun(n-1))
        
        res = recur_fun(n) 
        return res[k-1]
