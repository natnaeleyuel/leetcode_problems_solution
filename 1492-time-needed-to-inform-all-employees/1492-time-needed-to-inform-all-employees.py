class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manage_dict = defaultdict(list)
        for i in range(n):
            manage_dict[manager[i]].append(i)
        
        result = 0
        curr = 0
        def dfs(id, curr):
            nonlocal result
            curr += informTime[id]
            if curr > result:
                result = curr

            for manage_id in manage_dict[id]:
                    dfs(manage_id, curr)

        dfs(headID, curr)
        return result
            
