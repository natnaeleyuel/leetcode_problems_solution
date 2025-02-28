class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        left = 0
        l1 = m
        l2 = n
        for i in range(l1):
            while left < l2 and nums1[i] > nums2[left]:
                result.append(nums2[left])
                left += 1
            result.append(nums1[i])
        
        for i in range(left, l2):
            result.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = result[i]
            
        return nums1

        