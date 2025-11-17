class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ind1 = -1
        ind2 = -1
        for i in range(n):
            if nums[i] == 1:
                ind1 = ind2 
                ind2 = i

                if ind1 != -1 and ind2 - ind1 < k + 1:
                    return False
        
        return True