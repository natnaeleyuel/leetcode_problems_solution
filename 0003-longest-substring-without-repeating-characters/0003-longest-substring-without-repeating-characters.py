class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        n = len(s)
        new_set = set()
        for right in range(n):
            while s[right] in new_set:
                new_set.remove(s[left])
                left += 1
            cur_len = right - left + 1
            new_set.add(s[right])
            if cur_len > max_len:
                max_len = cur_len
        return max_len