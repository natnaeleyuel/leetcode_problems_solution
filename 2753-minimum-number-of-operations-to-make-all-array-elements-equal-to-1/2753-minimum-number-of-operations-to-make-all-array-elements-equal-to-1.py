class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while a and b:
                a = a % b
                b, a = a, b
            return max(a, b)

        ones = 0
        g = 0
        for num in nums:
            if num == 1:
                ones += 1
            g = gcd(g, num)
            
        if ones > 0:
            return len(nums) - ones
        if g != 1:
            return -1

        min_len = float("inf")
        for i in range(len(nums)):
            g = 0
            for j in range(i, len(nums)):
                if j - i + 1 >= min_len:
                    break
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = j - i + 1
                    break

        return (min_len - 1) + len(nums) - 1