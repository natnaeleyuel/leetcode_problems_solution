class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr2 = len(arr)
        arr3 = []
        for i in arr:
            if i == 0:
                arr3.append(0)
            arr3.append(i)


        arr.clear()
        arr.extend(arr3[:arr2])