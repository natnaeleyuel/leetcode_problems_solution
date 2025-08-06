class Solution:
    def reverseWords(self, s: str) -> str:
        tripped_s = s.strip()
        return " ".join(tripped_s.split()[::-1])