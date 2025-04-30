class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = Counter(tasks)
        heap = []
        for task, freq in freq_count.items():
            heappush(heap, -freq)
        
        interval = 0
        while heap:
            cycle = n + 1
            curr_time = 0
            processed = []
            while heap and cycle or processed and cycle:
                if heap:
                    freq = -heappop(heap)
                    freq -= 1
                    if freq:
                        processed.append(-freq)
                interval += 1
                cycle -= 1
            
            for freq in processed:
                heappush(heap, freq)
        
        return interval


