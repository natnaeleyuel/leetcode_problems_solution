class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameDict = {}
        for i in range(len(heights)):
            nameDict[heights[i]] = names[i]
        
        # for i in range(len(heights)):    # bubble sort
        #     isSorted = True
        #     for j in range(1, len(heights)):
        #         if heights[j] < heights[j-1]:
        #             heights[j], heights[j-1] = heights[j-1], heights[j]
        #             isSorted = False

        #     if isSorted:
        #         break

        # for i in range(len(heights)):     # selection sort
        #     minInd = i
        #     isSwap = False
        #     for j in range(i+1, len(heights)):
        #         if heights[minInd] > heights[j]:
        #             minInd = j
        #             isSwap = True

        #     if isSwap:
        #         heights[i], heights[minInd] = heights[minInd], heights[i]


        for i in range(len(heights)):       # selection sort
            for j in range(1, len(heights)):
                if heights[j] < heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]

        heights = heights[::-1]
        namesNew = [""]*len(names)
        for i in range(len(names)):
            namesNew[i] = nameDict[heights[i]]
        
        return namesNew