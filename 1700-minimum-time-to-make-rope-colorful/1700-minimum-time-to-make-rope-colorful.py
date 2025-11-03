class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        tot_time = 0
        temp = []
        time = []
        for i in range(n):
            if not temp:
                temp.append(colors[i])
                time.append(neededTime[i])
            else:
                if temp[-1] == colors[i]:
                    temp.append(colors[i])
                    time.append(neededTime[i])
                else:
                    if len(temp) > 1:
                        tot_time += sum(time) - max(time)
                    temp = [colors[i]]
                    time = [neededTime[i]]
        
        if len(temp) > 1:
            tot_time += sum(time) - max(time)

        return tot_time
        


                

