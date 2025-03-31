class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        arr = [weights[i+1] + weights[i] for i in range(n-1)]

        arr.sort()
        result = 0
        for i in range(k-1):
            result += arr[n - 2 - i] - arr[i]
        
        return result
