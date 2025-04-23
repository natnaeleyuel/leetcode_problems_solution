class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for num in range(1, n + 1):
            digit_sum = 0
            k = num
            while k != 0:
                digit_sum += k % 10
                k = k // 10
            d[digit_sum] += 1
        
        max_size = max(d.values())
        count = 0
        for size in d.values():
            if size == max_size:
                count += 1
        return count
