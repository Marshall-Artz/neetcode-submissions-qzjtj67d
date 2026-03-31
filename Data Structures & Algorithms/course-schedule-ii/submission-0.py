class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        completed = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        res = []
        def dfs(course) -> bool:
            if course in visited:
                return False
            if course in completed:
                return True
            
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            completed.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res