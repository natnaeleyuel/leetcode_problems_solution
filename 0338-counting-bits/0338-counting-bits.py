class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            k = int(bin(i)[2:])
            count = 0
            while k > 0:
                if k % 10 != 0:
                    count += 1
                k //= 10
            result.append(count)
        return result 