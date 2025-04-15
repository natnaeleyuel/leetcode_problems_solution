class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        arr = [0] * n
        for ind, num in enumerate(nums2):
            arr[num] = ind
        
        mp = [arr[v] for v in nums1]
        def update(curr, ind, v):
            while ind < len(curr):
                curr[ind] += v
                ind += ind & -ind

        def opr(curr, ind):
            tot = 0
            while ind > 0:
                tot += curr[ind]
                ind -= ind & - ind
            return tot

        l = [0] * n
        curr = [0] * (n + 2)
        for i in range(n):
            l[i] = opr(curr, mp[i])
            update(curr, mp[i] + 1, 1)
        
        r = [0] * n
        curr = [0] * (n + 2)
        for i in range(n-1, -1, -1):
            r[i] = opr(curr, n) - opr(curr, mp[i] + 1)
            update(curr, mp[i] + 1, 1)
        
        final = [l[i] * r[i] for i in range(n)]

        return sum(final)
        
        

