class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                i -= 1
                if i == -1 and digits[0] == 0:
                    digits = [1] + digits
        return digits