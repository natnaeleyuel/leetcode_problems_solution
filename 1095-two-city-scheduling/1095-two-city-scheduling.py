class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        new_arr = sorted(costs, key= lambda x: x[0] - x[1])
        result = 0
        for i in range(len(new_arr)):
            if i < len(new_arr) // 2:
                result += new_arr[i][0]
            else:
                result += new_arr[i][1]
        return result
        