class Solution:
    def frequencySort(self, s: str) -> str:
        chrCounter = Counter(s)
        sortedCounter = dict(sorted(chrCounter.items(), key= lambda item: item[1], reverse= True))
        
        newList = [count*(chrVal) for chrVal, count in sortedCounter.items()]

        return ''.join(newList)

