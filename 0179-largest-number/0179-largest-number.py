class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsStr = [str(nums[i]) for i in range(len(nums))]
        def comparator(a, b):
            val1 = a + b
            val2 = b + a
            if val1 < val2:
                return 1
            if val1 > val2:
                return -1
            return 0

        numsStr.sort(key = cmp_to_key(comparator))
        
        return str(int("".join(numsStr)))
                