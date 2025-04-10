class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(list)
        for node1, node2 in edges:
            edges_dict[node1].append(node2)
            edges_dict[node2].append(node1)
    
        visited = set()
        curr = []
        def dfs(node):
            curr.append(node)
            visited.add(node)
            for neigh in edges_dict[node]:
                if neigh not in visited:
                    dfs(neigh)

            return curr
        
        result = 0
        for i in range(n):
            if i not in visited:
                curr = dfs(i)
                cond = True
                for node in curr:
                    if len(curr) - 1 != len(edges_dict[node]):
                        cond = False
                curr = []
                if cond:
                    result += 1
        
        return result 
