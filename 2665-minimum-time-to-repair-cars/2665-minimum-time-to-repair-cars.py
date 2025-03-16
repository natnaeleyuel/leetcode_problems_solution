class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def repair(time):
            total = 0
            for rank in ranks:
                total += int((time // rank) ** 0.5)
                if total >= cars:
                    return True
            return total >= cars
        
        l = 0
        r = max(ranks) * cars ** 2
        while l < r:
            m = (r + l) // 2
            if repair(m):
                r = m
            else:
                l = m + 1
        
        return l