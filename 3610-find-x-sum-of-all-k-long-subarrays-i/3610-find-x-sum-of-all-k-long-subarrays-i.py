class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def solve():
            tot = 0
            lng = 0
            for ind, tup in enumerate(sort_occur):
                tot += sort_occur[ind][0] * sort_occur[ind][1]
                lng += 1
                if lng == x:
                    break
            res.append(tot)

        n = len(nums)
        m = n - k
        res = []
        occur = defaultdict(int)
        for i in range(k):
            occur[nums[i]] += 1

        sort_occur = sorted(occur.items(), reverse=True, key=lambda item: (item[1], item[0]))
        solve()

        for i in range(1, m + 1):
            if occur[nums[i-1]] == 1 and nums[k+i-1] != nums[i-1]:
                del occur[nums[i-1]]
            else:
                occur[nums[i-1]] -= 1
            occur[nums[k+i-1]] += 1
            sort_occur = sorted(occur.items(), reverse=True, key=lambda item: (item[1], item[0]))
            solve()
        
        return res
            
            
