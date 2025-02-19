class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(current_string):
            if len(current_string) == n:
                happy_string.append(current_string)
                return 
            
            for char in 'abc':
                if current_string and current_string[-1] == char:
                    continue
                dfs(current_string + char)
                
        happy_string = []
        dfs('')

        return '' if len(happy_string) < k else happy_string[k-1]