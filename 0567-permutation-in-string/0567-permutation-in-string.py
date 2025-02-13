class Solution(object):
    def checkInclusion(self, s1, s2):
        lenS1, lenS2 = len(s1), len(s2)
        if lenS1 > lenS2:
            return False
        
        countS1 = Counter(s1)
        countS2 = Counter(s2[:lenS1])
        
        if countS1 == countS2:
            return True
        
        for i in range(lenS1, lenS2):
            countS2[s2[i]] += 1
            countS2[s2[i - lenS1]] -= 1
            
            if countS2[s2[i - lenS1]] == 0:
                del countS2[s2[i - lenS1]]
            
            if countS1 == countS2:
                return True
        
        return False

             
        