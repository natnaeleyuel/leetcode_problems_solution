class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = n
        ind = 1

        while ind < n:
            if ratings[ind] == ratings[ind-1]:
                ind += 1
            
            peak = 0
            while ind < n and ratings[ind] > ratings[ind-1]:
                peak += 1
                result += peak
                ind += 1

            if ind == n:
                return result

            low = 0
            while ind < n and ratings[ind] < ratings[ind-1]:
                low += 1
                result += low
                ind += 1
            
            result -= min(peak, low)
        
        return result
