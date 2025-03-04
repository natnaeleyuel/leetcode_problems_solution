class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        result = 0
        for a, b in c.items():
            result += ceil(b/(a+1)) * (a + 1)
        return result