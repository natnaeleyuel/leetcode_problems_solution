class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.n = len(self.nums)
        self.heap = []
        for i in range(self.n):
            self.add(self.nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap_push(val)
        else:
            if val > self.heap[0]:
                self.heap_pop()
                self.heap_push(val)
        return self.heap[0]
        
    def heap_down(self, ind):
        smallest_ind = ind
        left = ind * 2 + 1
        right = left + 1
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest_ind]:
            smallest_ind = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest_ind]:
            smallest_ind = right
        if smallest_ind != ind:
            self.heap[smallest_ind], self.heap[ind] = self.heap[ind], self.heap[smallest_ind]
            self.heap_down(smallest_ind)
        
    def heap_up(self, ind):
        parent_ind = (ind - 1) // 2
        while ind > 0 and self.heap[ind] < self.heap[parent_ind]:
            self.heap[ind], self.heap[parent_ind] = self.heap[parent_ind], self.heap[ind]
            ind = parent_ind
            parent_ind = (ind - 1) // 2
    
    def heap_push(self, val):
        self.heap.append(val)
        self.heap_up(len(self.heap) - 1)

    def heap_pop(self):
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_down(0)

        return min_val
