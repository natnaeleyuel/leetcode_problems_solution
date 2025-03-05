class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            log = logs[i]
            if stack and log == '../':
                stack.pop()
            elif log != './' and log != '../':
                stack.append(log)
        
        return len(stack)