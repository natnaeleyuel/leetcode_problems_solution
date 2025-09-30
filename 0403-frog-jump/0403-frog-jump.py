class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache 
        def dfs(curr_ind:int, last_jump_dist:int) -> bool:
            if curr_ind == n-1:
                return True
            for next_jump_dist in range(last_jump_dist-1, last_jump_dist+2):
                target_pos = stones[curr_ind] + next_jump_dist
                if next_jump_dist > 0 and target_pos in pos_to_ind:
                    target_ind = pos_to_ind[target_pos]
                    if dfs(target_ind, next_jump_dist):
                        return True
            return False
        
        n = len(stones)
        pos_to_ind = {pos:ind for ind, pos in enumerate(stones)}
        return dfs(0, 0)
        
        