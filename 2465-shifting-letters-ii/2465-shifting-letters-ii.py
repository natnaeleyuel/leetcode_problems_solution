class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # arr = [0]*len(s)
        # for i in range(len(shifts)):
        #     for j in range(len(s)):
        #         if j >= shifts[i][0] and j <= shifts[i][1]:
        #             if shifts[i][2] == 0:
        #                 arr[j] -= 1
        #             elif shifts[i][2] == 1:
        #                 arr[j] += 1

        # new_s = list(s)
        # for i in range(len(new_s)):
        #     if arr[i] > 0:
        #         cur_ord = ord(new_s[i]) - 97 + arr[i]
        #         cur_ord = cur_ord % 26
        #         new_s[i] = chr(cur_ord + 97)
        #     elif arr[i] < 0:
        #         cur_ord = ord(new_s[i]) - 97 + arr[i]
        #         if cur_ord > 0:
        #             new_s[i] = chr(cur_ord + 97)
        #         else: 
        #             cur_ord = cur_ord % 26
        #             new_s[i] = chr(cur_ord + 97)
        

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