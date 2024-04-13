"""
Given n nodes labeled from 0 to n - 1 and a list of undirected 
edges (each edge is a pair of nodes), write a function to 
check whether these edges make up a valid tree.

Example 1:

    Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    
    Output: True

Example 2:

    Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

    Output: False

Note:

    You can assume that no duplicate edges will appear in edges. 
    
    Since all edges are undirected, [0, 1] is the same as [1, 0] and 
        thus will not appear together in edges.

Constraints:

    1 <= n <= 100
    0 <= edges.length <= n * (n - 1) / 2

Takeaway:

    We do not have loops in trees.
    
    A tree needs to be connected.

    DFS will help us out.
"""

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # we do not have loops in trees.
        # a tree needs to be connected.

        # in a dfs traversal, number of visited nodes
        # should match the input node size

        # edge case, empty graph is a tree
        if not n:
            return True

        # make an adjaceny list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                # node i was seen before!
                return False
            
            visit.add(i)
            
            for j in adj[i]:
                # for every neighbor
                if j == prev:
                    # go on
                    continue
                # make i as the new previous and call the dfs
                if not dfs(j, i):
                    # we detected a loop
                    return False
            return True

        # because -1 is not a node AND if no loop the lengths are equal
        return dfs(0, -1) and n == len(visit)
    
sol = Solution()
print(sol.validTree(n=5, edges=[[0,1],[0,2],[0,3],[1,4]]))
