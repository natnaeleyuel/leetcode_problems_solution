class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        cur_sum = 0
        m = len(cardPoints) - k
        for i in range(m):
            cur_sum += cardPoints[i]
        min_sum = cur_sum
        

        for right in range(m, len(cardPoints)): 
            cur_sum = cur_sum + cardPoints[right] - cardPoints[left]
            min_sum = min(min_sum, cur_sum)
            left += 1
        
        return sum(cardPoints) - min_sum
            
        


        