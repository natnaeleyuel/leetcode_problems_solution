class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverseArr(arr, j):
            i = 0
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1

        n = len(arr)
        result = []
        for i in range(n - 1, 0, -1):
            j = i
            while j > 0 and arr[j] != i + 1:
                j -= 1
            if j < i:
                if j > 0:
                    result.append(j + 1)
                    reverseArr(arr, j)
                result.append(i + 1)
                reverseArr(arr, i)
        return result

