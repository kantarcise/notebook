"""
There is an undirected graph with n nodes. 

There is also an edges array, where edges[i] = [a, b] means that there 
is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Example 1:

    Input: n=3, edges=[[0,1], [0,2]]
    
    Output: 1

Example 2:

    Input:  n=6, edges=[[0,1], [1,2], [2, 3], [4, 5]]
    
    Output: 2

Constraints:

    1 <= n <= 100
    
    0 <= edges.length <= n * (n - 1) / 2

Takeaway:

    Another chance to learn UnionFind.

    Both DFS and UnionFind will work.

    If you have the edges you can make you own adjacency list
"""

class Solution:

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """The dfs solution =) 
        """
        # [[0, 1], [0, 2]] 
        # single portion that is connected, result is 1

        # [[0, 1], [1, 2], [2, 3], [4, 5]]
        # 2 seperate connected portions, result is 2

        # Make an adjacency list
        adj_list = [[] for i in range(n)]

        # populate adj_list with edges:
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(node):
            # Mark the current node as visited
            visited[node] = True
            # Recur for all the vertices adjacent to this vertex
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Mark all the vertices as not visited
        visited = [False for _ in range(n)]

        # Store the number of connected components
        count = 0
         
        for v in range(n):
            if not visited[v]: # if (visited[n] == False):
                dfs(v)
                count += 1
                 
        return count
   
    def countComponents_(self, n: int, edges: list[list[int]]) -> int:
        """Union Find Solution"""
        # we will find parents of nodes

        # if two union condidate has same root parent
        # they are already connected
        # we will use rank as we union two nodes.

        # parent and rank will change as we 
        # iterate through nodes

        # initially all parents are nodes themselves
        parent = [i for i in range(n)]

        # rank is initially 1 for all
        rank = [1] * n

        def find(n):
            # initially the result is n
            res = n

            # until you get to node that is parent to itself
            while res != parent[res]:
                # path compression - shorten the path
                parent[res] = parent[parent[res]]
                # set result to the parent
                res = parent[res]
            # the node that is parent to itself
            return res

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                # p2 is the parent
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                # p1 is the parent
                parent[p2] = p1
                rank[p2] += rank[p1]

            # we actually did the union
            return 1

        # the result is initially n different nodes
        res = n
        for n1, n2 in edges:
            # every time we make a union, we decrease the result
            res -= union(n1, n2)

        return res
