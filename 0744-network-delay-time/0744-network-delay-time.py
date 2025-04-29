class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0

        graph = defaultdict(list)
        for node1, node2, time in times:
            graph[node1].append((node2, time))

        d = defaultdict(int)
        priority_queue = [(0, k)]
        for i in range(1, n + 1):
            d[i] = float('inf')
        d[k]  = 0
        while priority_queue:
            curr_time, node = heapq.heappop(priority_queue)
            for nei, time in graph[node]:
                new_time = curr_time + time
                if new_time < d[nei]:
                    d[nei] = new_time
                    heapq.heappush(priority_queue, (new_time, nei))

        max_time = max(d.values())
        return max_time if max_time != float('inf') else -1


