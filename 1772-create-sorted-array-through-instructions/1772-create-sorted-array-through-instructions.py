class Solution:
    MOD = 10**9 + 7
    def createSortedArray(self, instructions: List[int]) -> int:
        dictinst = defaultdict(int)
        sl = SortedList()
        result = 0
        
        for i in range(len(instructions)):
            dictinst[instructions[i]] += 1
            sl.add(instructions[i])
            if i == 0:
                result = result % self.MOD
            else:
                leftind = sl.bisect_left(instructions[i])
                low = leftind 
                high = len(sl) - low
                if dictinst[instructions[i]] > 0:
                    high -= dictinst[instructions[i]]
                result = (result + min(low, high)) % self.MOD
        return result