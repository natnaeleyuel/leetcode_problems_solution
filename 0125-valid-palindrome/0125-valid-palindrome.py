class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = "~`!@#$%^&*()_-+=[{]}\|;:'\",<.>/?"
        s = s.lower().replace(" ", "")
        for char in punc:
            s = s.replace(char,"")
        return (s == s[::-1])
