class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_dict = defaultdict(int)
        for row in grid:
            for col in row:
                nums_dict[col] += 1
        
        nums_dict = dict(sorted(nums_dict.items()))
        arr = [num for num, count in nums_dict.items()]
        count = [count for num, count in nums_dict.items()]
        prefix_sum = list(accumulate(count))
        prefix_sum2 = list(accumulate(count[::-1]))
        prefix_sum2 = prefix_sum2[::-1]
        
        pcs = [0] * len(arr)
        for i in range(1, len(arr)):
            if (arr[i] - arr[0]) % x != 0:
                return -1

        for i in range(1, len(arr)):
            pcs[i] = pcs[i-1] + (arr[i] - arr[i-1]) * prefix_sum[i-1]
        
        scs = [0] * len(arr)
        for i in range(len(arr) - 2, -1, - 1):
            scs[i] = scs[i+1] + (arr[i+1] - arr[i]) * prefix_sum2[i+1]
        
        result = float(inf)
        if len(arr) == 1:
            return 0
        for i in range(len(arr)):
            if i == 0:
                if scs[0] < result:
                    result = scs[i]
            elif i == len(arr) - 1:
                if pcs[i] < result:
                    result = pcs[i]
            else:
                if pcs[i] + scs[i] < result:
                    result = pcs[i] + scs[i]
        
        return result // x 