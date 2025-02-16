class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        a, b = float('inf'), float('inf')
        for val, count in nums_counter.items():
            if count == 1:
                if a == float('inf'):
                    a = val
                else:
                    b = val
        return [a, b]
