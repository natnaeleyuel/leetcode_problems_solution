class Solution:
    def minimumSteps(self, s: str) -> int:
        tot_oper = 0
        zeros = 0
        for right in range(len(s) - 1, -1, -1):
            if s[right] == "0":
                zeros += 1
            else:
                tot_oper += zeros
        return tot_oper
        
            
