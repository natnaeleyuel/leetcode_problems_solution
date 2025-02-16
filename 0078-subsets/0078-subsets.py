class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_create(k):
            if k == len(nums):
                result.append(new_arr[:])
                return
            else:
                new_arr.append(nums[k])
                subsets_create(k+1)
                new_arr.pop()
                subsets_create(k+1)

        result = []
        new_arr = []
        subsets_create(0)
        return result

