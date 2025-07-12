class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        d = [0] * (2 ** 10)
        d[0] = 1
        bm = 0
        result = 0
        for c in word:
            chr_ind = ord(c) - ord('a')
            bm ^= 1 << chr_ind
            result += d[bm]
            for i in range(10):
                result += d[bm ^ (1 << i)]
            d[bm] += 1
        return result