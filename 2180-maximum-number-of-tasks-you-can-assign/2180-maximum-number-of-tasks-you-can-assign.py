class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n1 = len(workers)
        n2 = len(tasks)
        def possible(m, p):
            i = 0
            queue = deque()
            for j in range(n1 - m, n1):
                ws = workers[j]
                while i < m and tasks[i] <= ws + strength:
                    queue.append(tasks[i])
                    i += 1
                
                if not queue:
                    return False
                if queue[0] <= ws:
                    queue.popleft()
                else:
                    if not p:
                        return False
                    p -= 1
                    queue.pop()
            return True
        
        low = 0
        high = min(n1, n2)
        while low < high:
            mid = (low + high + 1) // 2
            if possible(mid, pills):
                low = mid
            else:
                high = mid - 1
        
        return low