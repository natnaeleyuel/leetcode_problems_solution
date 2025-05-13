class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bt = x ^ y
        return bin(bt).count("1")