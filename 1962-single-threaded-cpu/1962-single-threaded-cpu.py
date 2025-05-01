class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result_order = []
        time = 0
        heap1 = []
        n = len(tasks)
        for i in range(n):
            task = tasks[i]
            heappush(heap1, (task[0], task[1], i))
        
        heap2 = []
        while heap1 or heap2:
            while heap1 and heap1[0][0] <= time:
                enq_time, proc_time, task = heappop(heap1)
                heappush(heap2, (proc_time, task))
            
            if heap2:
                proc_time, task = heappop(heap2)
                result_order.append(task)
                time += proc_time
            elif heap1:
                time = heap1[0][0]
        
        return result_order

