class Solution(object):
    def minSubarray(self, nums, p):
        sum_nums = sum(nums)
        rem = sum_nums % p
        if rem == 0:
            return 0
        
        ans = len(nums)
        prefix = 0
        prefixToIndex = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            prefix %= p
            target = (prefix - rem + p) % p
            if target in prefixToIndex:
                ans = min(ans, i - prefixToIndex[target])
            prefixToIndex[prefix] = i

        return -1 if ans == len(nums) else ans


        