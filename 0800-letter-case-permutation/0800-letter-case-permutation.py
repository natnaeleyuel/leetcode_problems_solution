class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = [c for c in s if c.isalpha()]
        letters_count = len(letters)        
        n = 1 << letters_count
        result = []
        for i in range(n):
            temp = list(s)
            pt = 0
            for j in range(len(temp)):
                if temp[j].isalpha():
                    if i & 1 << pt:
                        temp[j] = temp[j].upper()
                    else:
                        temp[j] = temp[j].lower()
                    pt += 1
            result.append(''.join(temp))
        
        return result
