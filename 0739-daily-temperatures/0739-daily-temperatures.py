class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        t = len(temperatures)
        tempdict = defaultdict(int)
        for i in range(t):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                prev = stack.pop()
                tempdict[prev] = i - prev
            stack.append(i)
             
        return [tempdict[ind] for ind in range(t)]
