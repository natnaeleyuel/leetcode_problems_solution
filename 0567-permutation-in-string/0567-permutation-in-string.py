from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dictS1 = Counter(s1)
        # difDict = defaultdict(int)
        # left = 0
        # right = len(s1) - 1
        # for i in range(right+1):
        #     difDict[s2[i]] += 1

        # while right < len(s2) and len(s1) <= len(s2):
        #     print(difDict)
        #     print(dictS1)
        #     if dictS1 == difDict:
        #         return True
        #     difDict[s2[right]] += 1
        #     difDict[s2[left]] -= 1

        #     right += 1
        #     left += 1
        # return False
        counter1 = Counter(s1)
        right=len(s1)-1
        left=0
        
        while right<len(s2):
            counter2 = Counter(s2[left:right+1])
            print(counter2)
            if counter2== counter1:
                return True
            left+=1
            right+=1
        return False


