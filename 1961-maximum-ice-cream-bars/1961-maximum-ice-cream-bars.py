class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ind = 0
        result = 0
        while ind < len(costs):
            if costs[ind] + result <= coins:
                result += costs[ind]
                ind += 1
            else:
                break

        return ind 
