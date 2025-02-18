class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def backtrack(index):
            nonlocal result
            if result:  
                return
            
            if index == len(pattern) + 1:
                result = ''.join(current_sequence)  
                return
            
            for num in range(1, 10): 
                if used[num]: 
                    continue
                
                if index > 0:
                    last_num = int(current_sequence[-1])
                    if pattern[index - 1] == 'I' and last_num >= num:
                        continue
                    if pattern[index - 1] == 'D' and last_num <= num:
                        continue
                
                used[num] = True
                current_sequence.append(str(num))
                
                backtrack(index + 1)
                
                used[num] = False
                current_sequence.pop()
        
        used = [False] * 10  
        current_sequence = [] 
        result = None  
        
        backtrack(0)
        
        return result
