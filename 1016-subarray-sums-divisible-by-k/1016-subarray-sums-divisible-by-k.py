class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        count_dict = defaultdict(int)
        count_dict[0] = 1
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            remain = cur_sum % k
            if remain in count_dict:
                result += count_dict[remain]
            count_dict[remain] += 1
        return result