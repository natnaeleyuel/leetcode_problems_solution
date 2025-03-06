class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        numsdict = {}
        for i, num in enumerate(nums1):
            numsdict[num] = i   
        result = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                if val in numsdict:
                    ind = numsdict[val]
                    result[ind] = nums2[i]

            stack.append(nums2[i])
        
        return result