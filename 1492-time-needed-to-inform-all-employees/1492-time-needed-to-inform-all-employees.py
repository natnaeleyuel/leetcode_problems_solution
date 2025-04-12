class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        
        result = 0
        curr = 0
        def dfs(id, curr):
            nonlocal result
            curr += informTime[id]
            if curr > result:
                result = curr

            for manage_id in graph[id]:
                    dfs(manage_id, curr)

        dfs(headID, curr)
        
        return result
            
