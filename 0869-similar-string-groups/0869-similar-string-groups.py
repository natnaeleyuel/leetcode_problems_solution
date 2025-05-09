class DisjointUnion:
        def __init__(self, size):
            self.rank = [0] * (size)
            self.root = [i for i in range(size)]
   
        def find(self, x):
            if x == self.root[x]:
                return x

            self.root[x] = self.find(self.root[x])
            return self.root[x]
   
        def union(self, x, y):
            rootx = self.find(x)
            rooty = self.find(y)
            if rootx != rooty:
                rankx = self.rank[rootx]
                ranky = self.rank[rooty]
                if rankx > ranky:
                    self.root[rooty] = rootx
                elif rankx < ranky:
                    self.root[rootx] = rooty
                else:
                    self.root[rooty] = rootx
                    self.rank[rootx] += 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        dsu = DisjointUnion(n)

        def check(str1, str2):
            l = len(str1)
            count_diff = 0
            for i in range(l):
                if str1[i] != str2[i]:
                    count_diff += 1
                    if count_diff > 2:
                        return False
            return True
        
        tot = n
        for i in range(n):
            for j in range(i + 1, n):
                str1 = strs[i]
                str2 = strs[j]
                root1 = dsu.find(i)
                root2 = dsu.find(j)
                if root1 != root2:
                    if check(str1, str2):
                        tot -= 1
                        dsu.union(i, j)
        
        return tot

        