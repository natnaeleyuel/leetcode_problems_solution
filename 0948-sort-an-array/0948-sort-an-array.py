class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            leftarr = []
            rightarr = []

            for i in range(left, mid + 1):
                leftarr.append(arr[i])
            
            for j in range(mid + 1, right + 1):
                rightarr.append(arr[j])

            i, j, k = 0, 0, left

            while i < n1 and j < n2:
                if leftarr[i] <= rightarr[j]:
                    arr[k] = leftarr[i]
                    i += 1
                else:
                    arr[k] = rightarr[j]
                    j += 1
                k += 1
            
            while i < n1:
                arr[k] = leftarr[i]
                i += 1
                k += 1
            
            while j < n2:
                arr[k] = rightarr[j]
                j += 1
                k += 1
        
        def mergesort(arr, left, right):
            if left >= right:
                return []
            mid = (left + right) // 2

            mergesort(arr, left, mid)
            mergesort(arr, mid + 1, right)
            merge(arr, left, mid, right)
        

        mergesort(nums, 0, len(nums) - 1)
        return nums