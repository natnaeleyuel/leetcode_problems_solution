class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = [0] * n
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            choose = points
            skip = 0
            next_i = i + brainpower + 1
            if next_i < n:
                choose += cache[next_i]
            if i + 1 < n:
                skip = cache[i + 1]
            cache[i] = max(choose, skip)

        return cache[0]