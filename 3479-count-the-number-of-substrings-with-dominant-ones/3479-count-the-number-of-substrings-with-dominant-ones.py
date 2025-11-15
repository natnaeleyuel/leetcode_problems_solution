class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        next_zero = [n] * (n + 1)
        for i in range(n - 2, -1, -1):
            if s[i + 1] == "0":
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]

        result = 0
        for i in range(n):
            zeroes = 1 if s[i] == "0" else 0
            j = i

            while zeroes ** 2 <= n:
                next_j = next_zero[j]
                ones = (next_j - i) - zeroes

                if ones >= zeroes ** 2:
                    result += min(
                        next_j - j,
                        ones - zeroes ** 2 + 1
                    )

                j = next_j
                zeroes += 1

                if j == n:
                    break

        return result
