class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = Counter(nums)
        arr = [i for i, count in c.items() if count == 1]
        if k == 1:
            if len(arr) > 0:
                return max(arr)
            else:
                return -1
        elif k == n:
            return max(nums)
        elif k > 1 and k < n:
            if c[nums[0]] == 1:
                if c[nums[-1]] == 1:
                    return max(nums[-1], nums[0])
                else:
                    return nums[0]
            else:
                if c[nums[-1]] == 1:
                    return nums[-1]
                else:
                    return -1