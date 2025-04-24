class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for cr, pr, in prerequisites:
            graph[pr].append(cr)
            in_degree[cr] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        while queue:
            pr = queue.popleft()
            result.append(pr)
            for cr in graph[pr]:
                in_degree[cr] -= 1
                if in_degree[cr] == 0:
                    queue.append(cr)
        
        return result if len(result) == numCourses else []



