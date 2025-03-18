class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def powerTwo(n, base):
            result = 2 ** base
            if result < n:
                base += 1
                return powerTwo(n, base)
            elif result == n:
                return base
            else:
                return base - 1

        def makePowerOfTwo(n):
            num_set = set()
            k = powerTwo(n, 0)
            sum_nums = 0
            for i in range(k+1 - 1, - 1, - 1):  
                if sum_nums + 2 ** i <= n: 
                    sum_nums += 2 ** i 
                    num_set.add(2**i)
            return num_set

        deq = deque()
        nums_set = set()
        max_len = 0
        for i in range(len(nums)):
            curr = nums[i]
            div = makePowerOfTwo(curr)
            l = len(nums_set.intersection(div))
            if l == 0:
                nums_set = nums_set.union(div)
                deq.append(curr)
            else:
                while len(nums_set.intersection(div)) != 0:
                    removed_num = deq.popleft()
                    removed_div = makePowerOfTwo(removed_num)
                    nums_set -= removed_div
                nums_set = nums_set.union(div)
                deq.append(curr)
            max_len = max(max_len, len(deq))
        
        return max_len
                
            
