"""
There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to 
take course ai.

    For example, the pair [0, 1], indicates that to take course 
0 you have to first take course 1.

Return the ordering of courses you should take to finish 
all courses. If there are many valid answers, return any 
of them. If it is impossible to finish all courses, 
return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]

Output: [0,1]

Explanation: There are a total of 2 courses to take. To take 
course 1 you should have finished course 0. So the 
correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]

Explanation: There are a total of 4 courses to take. To 
take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.

So one correct course order is [0,1,2,3].
Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.

Takeaway:

Fantastic way to learn topological sort.

We can make an adjacency list with a dict

"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """Return the order of courses based on prerequisites"""
        
        # this question teaches topological sort
        # which is a graph algorithm
        # vertice - node & edge - path
        # if we detect a cycle we will stop the run immediately,
        # no need to continue
        
        # we will make an adjacency list
        pre_map = {i: [] for i in range(numCourses)}
        
        # populate the map
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # a course has 3 possible states
        # visited: course has been added to output
        # visiting: course has not been added to output, but it is in the cycle
        # unvisited: course not added to output or cycle
        
        output = []
        visited, cycle = set(), set()
            
        # we can use dfs 
        # which we will use on every course
        def dfs(crs):
            if crs in cycle:
                # detected a cycle
                return False
            if crs in visited:
                # we do not need to visit this again
                # this is because we will run dfs on 
                # every course, which might result in repeated work
                return True
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) == False:
                    # we detected a cycle
                    return False
                
            # now we can remove the course from cycle
            cycle.remove(crs)
            # we went through all prerequisites
            # we can add this to visited
            visited.add(crs)
            # now that we actually visited all prerequisites
            # we can add it to output
            output.append(crs)
            
            return True
        
        # run dfs on all courses
        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        # if all dfs run successfully
        # return the output we built!
        return output
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0, 1, 2, 3]