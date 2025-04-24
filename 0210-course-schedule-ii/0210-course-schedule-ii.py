class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for cr, pr, in prerequisites:
            graph[pr].append(cr)

        colors = [0] * numCourses
        result = []
        for node in range(numCourses):
            if colors[node] != 0:
                continue
            if not self.topSort(node, result, graph, colors):
                return []

        return result[::-1]

    def topSort(self, node, result, graph, colors):
        if colors[node] == 1:
            return False
        
        colors[node] = 1
        for course in graph[node]:
            if colors[course] == 2:
                continue
            if not self.topSort(course, result, graph, colors):
                return False
            
        result.append(node)
        colors[node] = 2
        return True



