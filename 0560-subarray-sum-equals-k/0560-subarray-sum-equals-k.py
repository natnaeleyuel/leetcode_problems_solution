class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        cur_sum = 0
        result = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if (cur_sum - k) in prefix_sum:
                result += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] += 1
        return result

