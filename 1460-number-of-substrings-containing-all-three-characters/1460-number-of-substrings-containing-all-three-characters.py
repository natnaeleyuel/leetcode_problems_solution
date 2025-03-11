class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = {'a':0, 'b':0, 'c':0}
        result = 0
        left = 0
        right = 0
        while right < n:
            count[s[right]] += 1
            while all(count.values()):
                result += n - right
                count[s[left]] -= 1
                left += 1
            right += 1
        return result


