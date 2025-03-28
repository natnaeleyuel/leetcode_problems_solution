class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def helper(rad):
            ho = 0
            he = 0
            while ho < len(houses) and he < len(heaters):
                if abs(houses[ho] - heaters[he]) <= rad:
                    ho += 1
                else:
                    he += 1
            return ho == len(houses)
        
        houses.sort()
        heaters.sort()
        low = 0
        high = max(houses[-1], heaters[-1])

        while low < high:
            mid = low + (high - low) // 2
            if helper(mid):
                high = mid
            else:
                low = mid + 1
        return low