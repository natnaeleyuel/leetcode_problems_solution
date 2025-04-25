class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        queue = deque([])
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
        
        all_pr = [set() for i in range(numCourses)]
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                in_degree[nei] -= 1
                all_pr[nei].add(node)
                all_pr[nei].update(all_pr[node])
                if in_degree[nei] == 0:
                    queue.append(nei)
                
        return [pr in all_pr[course]  for pr, course in queries]
