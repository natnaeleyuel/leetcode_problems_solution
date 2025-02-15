class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        sumDict = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sumDict[nums1[i] + nums2[j]] += 1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                result += sumDict[-nums3[i] - nums4[j]]
        
        return result


        
