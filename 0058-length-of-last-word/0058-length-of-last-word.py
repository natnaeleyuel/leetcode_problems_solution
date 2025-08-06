class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_s = s.strip()
        return len(trimmed_s.split(" ")[-1])