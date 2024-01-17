"""
There are a total of numCourses courses you have to take, labeled 
from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 
0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]

Output: false

Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take 
course 0 you should also have finished course 1. 
So it is impossible.

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

Takeaway:

We can make an adjecancy list using a hashmap

we will check the possible cycles with a set.

Because the graph is not connected, we have to run 
dfs on every course =)

"""
from collections import defaultdict

class Solution:
    def canFinish_(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # this was my first attempt
        # failed
        
        """Return True if one can 
        finish their courses"""
        # prerequisites
        # [a, b]
        # we must take b before a
        
        # we will have paths from prerequisites
        # and if there are disagreements, we cannot finish it.
        
        result = []
        # kinda like a directed arrows
        # [[1, 0], [4, 5], [5, 3], [2, 1]]
        # we can concatenate paths that are intersecting 
        for end, start in prerequisites:
            if [end, start] not in result:
                result.append([end, start])
            if start in [prerequisites[i][1] for i in range(len(prerequisites))]:
                # concatenate paths and add it to result
                result.append()
               

        def is_paths_crossing(seq):
            pass

        return False if is_paths_crossing(result) else True
    
    def canFinish__(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Return True if one can finish their courses
        This solution works but it is complex"""
        # Make a graph to represent the 
        # courses and their prerequisites
        graph = defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)

        # Helper function to perform DFS and detect cycles
        def is_cyclic(course, visited, path):
            visited[course] = True
            path[course] = True

            # Explore neighbors
            for neighbor in graph[course]:
                if not visited[neighbor]:
                    if is_cyclic(neighbor, visited, path):
                        return True
                elif path[neighbor]:
                    return True

            # Backtrack
            path[course] = False
            return False

        # Check for cycles in each course's prerequisites
        visited = [False] * numCourses
        path = [False] * numCourses

        for course in range(numCourses):
            if not visited[course]:
                if is_cyclic(course, visited, path):
                    return False
                
        # If there are no cycles, it is possible to finish all courses
        return True            

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Return True if one can finish their courses
        This one is the simplest approach"""
        # neet guidance
        # all courses and it's prequisites are edges 
        # time complexity is O(n + p) because we will move from 
        # every single node using every single edge
        
        # for [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
        # we will make an adjacency list
        # which we can implement with a hashmap
        
        # map = { course: prequisites}
        # 0 - [1, 2]
        # 1 - [3, 4]
        # 2 - []
        # 3 - [4]
        # 4 - []
        pre_map = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        # how can we detect loops?
        # we can use a set
        # just to check the visited courses
        # if we bump into already visited set, that means we found a loop!
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                # found a loop
                return False
            if pre_map[crs] == []:
                # no prerequisites
                # we can complete this course
                return True
            
            visited.add(crs)
            
            # otherwise, we have some work to do on prerequisites
            for elem in pre_map[crs]:
                if not dfs(elem):
                    # we do not have to wait if 
                    # we find 1 False
                    # just return False
                    return False
                
            # we finished visiting this course
            visited.remove(crs)
            
            # set it to an empty list so that we 
            # do not have to do all the work again
            pre_map[crs] = []
            return True
        
        # we have to manually run dfs on every single course
        # because the graph can be not connected
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True