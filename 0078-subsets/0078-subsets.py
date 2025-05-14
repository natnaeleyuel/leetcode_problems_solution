class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1, Backtracking solution 
        # def subsets_create(k):
        #     if k == len(nums):
        #         result.append(new_arr[:])
        #         return
        #     else:
        #         new_arr.append(nums[k])
        #         subsets_create(k+1)
        #         new_arr.pop()
        #         subsets_create(k+1)

        # result = []
        # new_arr = []
        # subsets_create(0)
        # return result

        # 2, Biwise solution 
        n = len(nums)
        tot = 1 << n
        result = []
        for i in range(tot):
            ss = []
            for j in range(n):
                if i & (1 << j):
                    ss.append(nums[j])
            result.append(ss)
        
        return result




