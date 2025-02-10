class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameDict = {}
        for i in range(len(heights)):
            nameDict[heights[i]] = names[i]
        
        for i in range(len(heights)):
            isSorted = True
            for j in range(1, len(heights)):
                if heights[j] < heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                    isSorted = False

            if isSorted:
                break
        
        heights = heights[::-1]
        namesNew = [""]*len(names)
        for i in range(len(names)):
            namesNew[i] = nameDict[heights[i]]
        
        return namesNew