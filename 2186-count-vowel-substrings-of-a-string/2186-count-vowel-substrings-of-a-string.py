class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0 
        dict = defaultdict(int)
        for i, x in enumerate(word): 
            if x in "aeiou": 
                if not i or word[i-1] not in "aeiou": 
                    k = i 
                    j = i
                    dict.clear()
                dict[x] += 1
                while len(dict) == 5 and all(dict.values()): 
                    dict[word[j]] -= 1
                    j += 1
                result += j - k
        return result 
