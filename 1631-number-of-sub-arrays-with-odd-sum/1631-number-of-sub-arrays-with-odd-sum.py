class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        prefix_sum = list(accumulate(arr))
        even_count = 1
        odd_count = 0
        MOD = 10**9 + 7
        for i in range(len(prefix_sum)):
            cur_sum = prefix_sum[i]
            if cur_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1
                
        return result 

