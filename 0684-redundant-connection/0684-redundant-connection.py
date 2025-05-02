class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            
            return root[x]
        
        root = [i for i in range(1010)]
        for node1, node2 in edges:
            if find(node1) == find(node2):
                return [node1, node2]
            root[find(node1)] = find(node2)
        
        return []


