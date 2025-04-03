class Solution:
    result = 0
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        def merge(leftarr, rightarr):
            i = 0
            j = 0
            while i < len(leftarr) and j < len(rightarr):
                if leftarr[i] <= rightarr[j] + diff:
                    self.result += len(rightarr) - j
                    i += 1
                else:
                    j += 1
                
            l = 0
            r = 0

            mergedarr = []
            while l < len(leftarr) and r < len(rightarr):
                if leftarr[l] < rightarr[r]:
                    mergedarr.append(leftarr[l])
                    l += 1
                else:
                    mergedarr.append(rightarr[r])
                    r += 1
            
            while l < len(leftarr):
                mergedarr.append(leftarr[l])
                l += 1

            while r < len(rightarr):
                mergedarr.append(rightarr[r])
                r += 1

            return mergedarr

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            leftarr = mergesort(arr[:mid])
            rightarr = mergesort(arr[mid:])

            return merge(leftarr, rightarr)
        
        mergesort(arr)

        return self.result
