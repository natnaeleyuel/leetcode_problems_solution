class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0
        for i in range(n-2):
            numi = arr[i]
            for j in range(i+1, n-1):
                numj = arr[j]
                for k in range(j + 1, n):
                    numk = arr[k]
                    if abs(numi - numj) <= a and abs(numj - numk) <= b and abs(numi - numk) <= c:
                        result += 1
        return result