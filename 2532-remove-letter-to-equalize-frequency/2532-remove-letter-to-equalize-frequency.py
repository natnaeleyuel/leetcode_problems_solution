class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        for i in c.keys():
            c[i] -= 1
            if len(set(val for val in c.values() if val)) == 1:
                return True
            c[i] += 1
        return False