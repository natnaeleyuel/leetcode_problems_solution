class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        higher_node = list(range(n))
        min_cost = [-1] * n
        def recur(node):
            if higher_node[node] != node:
                higher_node[node] = recur(higher_node[node])
            return higher_node[node]
        
        for src, tg, weight in edges:
            src_root = recur(src)
            tg_root = recur(tg)
            
            min_cost[tg_root] &= weight
            
            if src_root != tg_root:
                min_cost[tg_root] &= min_cost[src_root]
                higher_node[src_root] = tg_root
        
        arr = []
        for l, r in query:
            if l == r:
                arr.append(0)
            elif recur(l) != recur(r):
                arr.append(-1)
            else:
                arr.append(min_cost[recur(l)])
                
        return arr