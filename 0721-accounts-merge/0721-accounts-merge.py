class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = UnionFind(n)

        ownedby = defaultdict(int)
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownedby:
                    dsu.union(i, ownedby[email])
                ownedby[email] = i
        
        d = defaultdict(list)
        for email, owner in ownedby.items():
            d[dsu.find(owner)].append(email)

        result = [[accounts[i][0]] + sorted(emails) for i, emails in d.items()]
        return result

