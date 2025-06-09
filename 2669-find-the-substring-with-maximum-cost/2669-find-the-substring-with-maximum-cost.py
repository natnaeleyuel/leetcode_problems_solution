class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_to_val = {c: v for c, v in zip(chars, vals)}
        max_sum = current_sum = 0
        
        for c in s:
            val = char_to_val.get(c, ord(c) - 96)  
            current_sum = max(0, current_sum + val)
            max_sum = max(max_sum, current_sum)
        
        return max_sum