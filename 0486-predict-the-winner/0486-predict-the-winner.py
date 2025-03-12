class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        nums_dict = {}
        def recur(i, j):
            if (i, j) in nums_dict:
                return nums_dict[(i, j)]
            if i > j:
                return 0
            
            semi1 = nums[i] + min(recur(i+1, j-1), recur(i+2, j))
            semi2 = nums[j] + min(recur(i, j-2), recur(i+1, j-1))
            semiscore = max(semi1, semi2)
            nums_dict[(i, j)] = semiscore
            return semiscore
        
        n = len(nums) - 1
        recur_res = recur(0, n)
        return recur_res >= sum(nums) - recur_res
