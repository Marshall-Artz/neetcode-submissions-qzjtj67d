class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visiting = set()
        completed = set()

        def dfs(course) -> bool:
            if course in visiting:
                return False
            if course in completed or course not in graph:
                return True
            
            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            completed.add(course)
            
            return True

        # Load courses into dictionary
        for rel in prerequisites:
            course, prereq = rel[0], rel[1]
            graph[course].append(prereq)
        
        # Loop through courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True