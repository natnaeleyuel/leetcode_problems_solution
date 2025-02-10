class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def merge(nums, l, m, r):
            num1 = m + 1 - l
            num2 = r - m

            listLeft = [0] * num1
            listRight = [0] * num2

            for i in range(num1):
                listLeft[i] = nums[l + i]
            for j in range(num2):
                listRight[j] = nums[m + j + 1]
            
            i = 0
            j = 0
            k = l

            while i < num1 and j < num2:
                if listLeft[i] <= listRight[j]:
                    nums[k] = listLeft[i]
                    i += 1
                else:
                    nums[k] =  listRight[j]
                    j += 1
                k += 1
            
            while i < num1:
                nums[k] = listLeft[i]
                i += 1
                k += 1
             
            while j < num2:
                nums[k] = listRight[j]
                j += 1
                k += 1

        def mergeSort(nums, l, r):
            if l < r:
                m = l + (r-l) // 2

                mergeSort(nums, l, m)
                mergeSort(nums, m + 1, r)
                merge(nums, l, m, r)
        
        mergeSort(nums, 0, n-1)
        return nums