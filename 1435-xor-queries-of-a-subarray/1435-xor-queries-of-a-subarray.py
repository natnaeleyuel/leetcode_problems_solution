class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [arr[0]]
        n = len(arr)
        for i in range(1, n):
            xors.append(xors[-1] ^ arr[i])
        
        result = []
        for left, right in queries:
            if left:
                result.append(xors[right] ^ xors[left - 1])
            else:
                result.append(xors[right])
        
        return result