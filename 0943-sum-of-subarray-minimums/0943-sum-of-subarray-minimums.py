class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            k = -1 if not stack else stack[-1]
            result[i] = result[k] + arr[i] * (i - k)
            stack.append(i)
        return sum(result) % (10**9 + 7)