from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list to represent the directed graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Step 2: Create an array "indegrees" to store the number of incoming edges for each node in the graph
        indegrees = [0] * numCourses
        for prereq, _ in prerequisites:
            indegrees[prereq] += 1
        
        # Step 3: Add all the nodes with indegree 0 to a queue
        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        # Step 4: Topological Sort
        while queue:
            course = queue.popleft()
            for prereq in graph[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    queue.append(prereq)
        
        # Step 5: Check if we have removed all the courses successfully
        return all(indegree == 0 for indegree in indegrees)