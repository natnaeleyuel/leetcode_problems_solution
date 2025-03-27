class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant_num = [0] * len(nums) 
        dominant_num[-1] = nums[-1]
        dominant_num2 = [0] * len(nums)
        dominant_num2[0] = nums[0]
        nums_dict = defaultdict(int)
        nums_dict2 = defaultdict(int)
        nums_dict[nums[-1]] = 1
        nums_dict2[nums[0]] = 1

        for i in range(len(nums) - 2, -1, -1):
            nums_dict[nums[i]] += 1
            if nums_dict[nums[i]] > nums_dict[dominant_num[i+1]]:
                dominant_num[i] = nums[i]
            else:
                dominant_num[i] = dominant_num[i+1]

        for i in range(1, len(nums)):
            k = len(nums) - i 
            k2 = i
            nums_dict[nums[i-1]] -= 1

            val = dominant_num[i]
            val2 = dominant_num2[i-1]
            count = nums_dict[val]
            count2 = nums_dict2[val2]

            if dominant_num2[i-1] == dominant_num[i]:
                if 2 * count > k and 2 * count2 > k2:
                    return i - 1

            nums_dict2[nums[i]] += 1
            if nums_dict2[nums[i]] > nums_dict2[dominant_num2[i-1]]:
                dominant_num2[i] = nums[i]
            else:
                dominant_num2[i] = dominant_num2[i-1]
        
        return -1


