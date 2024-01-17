"""
In this problem, a tree is an undirected graph that is 
connected and has no cycles.

You are given a graph that started as a tree with n nodes 
labeled from 1 to n, with one additional edge added. The added 
edge has two different vertices chosen from 1 to n, and was not 
an edge that already existed. The graph is represented as an 
array edges of length n where edges[i] = [ai, bi] indicates that 
there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph 
is a tree of n nodes. If there are multiple answers, return 
the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
Constraints:

    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.

Takeaway:

This question is a great opportunity to learn about UnionFind

We need to find parent of nodes and union them if they 
do not have the same parents. While doing that we will 
update their ranks in order to union on a condition.

"""
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # tree - undirected graph that is connected and has no cycles.

        # Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
        # If there are multiple answers, return the answer that occurs 
        # last in the input.

        # we will start from the initial edge
        
        # we can use dfs to get O(n^2) solution
        # but we can use "Union Find" algorithm to get the solution in O(n)
        
        # in the beginning the graph will be connected anyway
        # because we will have n edges and n nodes
        
        # how can we decide if we made a cycle with adding an edge ?
        # when we add an edge, the nodes are ALREADY Connected
        
        # when we add a redundant connection (which is why the question 
        # is called Redundant Connection)

        # for every node, the parent is itself at the start
        parent = [i for i in range(len(edges) + 1)]
        
        # ranks is the amount of children every node has
        # initially 1 for all of them
        ranks = [1] * (len(edges) + 1)
        
        def find(n):
            """Given a node n, find what it's parent is."""
            # there could be multiple links to get to the root parent
            p = parent[n]
            
            # n could be the parent of itself, 
            # so we will keep going until we find the parent equals to self
            while p != parent[p]:
                # path compression
                # shorten the path as we go up the link
                parent[p] = parent[parent[p]]
                # go up the link
                p = parent[p]
            
            # once we got to the root parent
            return p
        
        def union(n1, n2):
            """Union two given nodes"""
            # to union two nodes we need to find 
            # both of the parents first
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                # they already have the same parent
                # we cannot union these two
                # we found a redundant connection
                return False
            
            # union them by ranks
            if ranks[p1] > ranks[p2]:
                # p1 is going to be the parent
                parent[p2] = p1
                # update the rank of p1
                ranks[p1] = ranks[p1] + ranks[p2]
            else:
                # do the opposite - p2 is parent
                parent[p1] = p2
                # update the rank of p2
                ranks[p2] += ranks[p1]
            
            # successfully union them 
            return True
        
        for n1, n2 in edges:
            # call union on n1, n2
            if not union(n1, n2):
                # if cannot union it 
                return [n1, n2]
