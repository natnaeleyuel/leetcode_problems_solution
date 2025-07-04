class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        ins = []
        outs = []
        seats = {}

        emptySeats = []
        nextSeat = 0

        for (i, val) in enumerate(times):
            ins.append((val[0], i))
            outs.append((val[1], i))

        ins.sort()
        outs.sort()

        for (time, friend) in ins:
            while outs[0][0] <= time:
                heapq.heappush(emptySeats, seats[outs[0][1]])
                outs.pop(0)

            if emptySeats:
                seats[friend] = heapq.heappop(emptySeats)
            else:
                seats[friend] = nextSeat
                nextSeat += 1
            
            if friend == targetFriend:
                break

        return seats[targetFriend]