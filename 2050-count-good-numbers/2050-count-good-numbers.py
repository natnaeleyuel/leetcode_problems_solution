class Solution:
    MOD = 10 ** 9 + 7
    def countGoodNumbers(self, n: int) -> int:

        def helper(m1, m2):
            rem = 1
            comp = m1
            while m2 > 0:
                if m2 % 2 == 1:
                    rem = rem * comp % self.MOD
                comp = comp * comp % self.MOD
                m2 //= 2
            return rem
        
        return helper(5, (n + 1) // 2) * helper(4, n // 2) % self.MOD

