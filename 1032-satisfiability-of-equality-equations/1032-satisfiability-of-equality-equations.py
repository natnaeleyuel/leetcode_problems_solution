class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = defaultdict()
        diff = []

        def find(x):
            if x not in root: 
                return x
            else: 
                return find(root[x])

        for curr in equations:             
            a, b = curr[0], curr[3]

            if curr[1] == "=":             
                x, y = find(a), find(b)
                if x != y:
                    root[y] = x
            else:    
                diff.append((a,b))      

        return all(find(a) != find(b) for a, b in diff)