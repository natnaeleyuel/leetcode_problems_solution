class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d_cost = defaultdict(int)
        for i in range(len(bills)):
            cost = bills[i]
            d_cost[cost] += 1
            if cost == 10:
                if d_cost[5] >= 1:
                    d_cost[5] -= 1
                else:
                    return False
            
            if cost == 20:
                if d_cost[10] >= 1:
                    if d_cost[5] >= 1:
                        d_cost[10] -= 1
                        d_cost[5] -= 1
                        d_cost[20] -= 1
                    else:
                        return False
                else:
                    if d_cost[5] >= 3:
                        d_cost[5] -= 3
                        d_cost[20] -= 1
                    else:
                        return False
        return True