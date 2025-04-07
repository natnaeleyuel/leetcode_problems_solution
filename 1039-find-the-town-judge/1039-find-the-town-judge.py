class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        count = defaultdict(int)
        edge_dict = defaultdict(list)
        for node1, node2 in trust:
            count[node2] += 1
            edge_dict[node1].append(node2)
        
        for node, count in count.items():
            if count == n - 1 and len(edge_dict[node]) == 0:
                return node
        
        return -1
