class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # optimized way using prefix sum
        n = len(s)
        diff = [0] * (n + 1)
        for left, right, direction in shifts:
            if direction == 0:
                diff[left] -= 1
                if right + 1 < n:
                    diff[right + 1] += 1
            
            else:
                diff[left] += 1
                if right + 1 < n:
                    diff[right + 1] -= 1
        
        result = ['']*n
        prefix_sum = 0
        for i in range(n):
            prefix_sum += diff[i]
            cur_ord = ord(s[i]) + prefix_sum - 97
            cur_ord = cur_ord % 26
            cur_chr = chr(cur_ord + 97)

            result.append(cur_chr)

        return ''.join(result)