class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            count = 0
            for j in nums:
                if i != j and i > j:
                    count += 1
            output.append(count)
        return output
        