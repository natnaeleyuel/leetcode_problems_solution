class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        c = Counter(nums)
        def findAllPermutations(res):
            if len(res) == len(nums):
                perm.append(res)
                return 
            
            for k in c:
                    if c[k]:
                        c[k]-=1
                        findAllPermutations(res + [k])    
                        c[k]+=1
                
        findAllPermutations([])
        return perm