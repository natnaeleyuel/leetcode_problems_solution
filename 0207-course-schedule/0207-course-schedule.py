class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        white = 1
        gray = 2 
        black = 3
        validiate = [white for i in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        def dfs(node):
            validiate[node] = gray
            res = True
            for neigh in graph[node]:
                if validiate[neigh] == white:
                    res = res & dfs(neigh)
                elif validiate[neigh] == gray:
                    return False
            validiate[node] = black
            return res
        ans = True
        for node in range(numCourses):
            if validiate[node] == gray:
                return False
            elif validiate[node] == white:
                ans = ans and dfs(node)
        return ans
            



        