class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        max_len = max(len(nums1), len(nums2))
        for i in range(max_len):
            if i < len(nums1):
                ids = nums1[i][0] 
                val = nums1[i][1]
                d[ids] += val

            if i < len(nums2):
                ids = nums2[i][0] 
                val = nums2[i][1]
                d[ids] += val
        
        d = dict(sorted(d.items(), key=lambda item: item[0]))
        merge = [[ids, val] for ids, val in d.items()]
        
        return merge