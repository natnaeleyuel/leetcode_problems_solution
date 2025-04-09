"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = defaultdict(int)
        subordinates = defaultdict(list)
        for employe in employees:
            importance[employe.id] = employe.importance
            subordinates[employe.id].extend(employe.subordinates)
        
        visited = set()
        def dfs(id):
            visited.add(id)
            for subord in subordinates[id]:
                if subord not in visited:
                    importance[id] += dfs(subord)

            return importance[id]
        
        dfs(id)
        return importance[id]


            
        