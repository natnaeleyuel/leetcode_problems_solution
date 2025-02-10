class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums.sort
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

        # '30', '3'
        # 303, 330
        # for i in range(len(numsStr)):
        #     maxInd = i
        #     minLen = len(numsStr[i])
        #     for j in range(i, len(numsStr)):
        #         minLen = min(minLen, len(numsStr[j]))
        #         if int(numsStr[maxInd][-minLen:]) < int(numsStr[j][-minLen:]):
        #             maxInd = j
            
        #     numsStr[i], numsStr[maxInd] = numsStr[maxInd], numsStr[i]
        
        # return ''.join(numsStr)
                