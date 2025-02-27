class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_length = 0
        s = set(arr)
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                l = arr[i]
                r = arr[j]
                curr = 0
                while l + r in s:
                    curr += 1
                    l, r = r, l + r

                max_length = max(max_length, curr + 2)
        return max_length if max_length > 2 else 0

