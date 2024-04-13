"""
You are given an array points representing integer coordinates 
of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the 
manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. 

All points are connected if there is exactly one simple path between 
any two points.

Example 1:

    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    
    Output: 20
    
    Explanation: 

        We can connect the points as shown above to get the minimum cost of 20.
        Notice that there is a unique path between every pair of points.

Example 2:

    Input: points = [[3,12],[-2,5],[-4,1]]
    
    Output: 18

Constraints:

    1 <= points.length <= 1000

    -10^6 <= xi, yi <= 10^6

    All pairs (xi, yi) are distinct.

Takeaway:

    MST for Prim's !

    BFS - visit set, [cost, node] 
"""

from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # neet, works!

        # when we are asked about min cost, we can think of MST
        # Minimum spanning Trees
        
        # where are the edges ? we have to find adj list
        
        # apply prims later
        
        # Prims algo:
        
        #   for n node, we need n - 1 edges to make a 
        #   MST without a cycle
        #   but we also want smallest edges
        
        #   we can start from any node we want, 
        #   we will run  a BFS using a visited hashset
        
        #   we will have frontiers, basically any node
        #   that is reacheble from start
        
        #   we will add to frontiers in the type of:
        #   (weight, node) so that we can pop based on whatever node 
        #   we can connect next with smallest cost
        
        #   when len(visit set) is equal to nodes, we are done!
        
        N = len(points)
        
        # i : list of [cost, node]        
        adj = {i:[] for i in range(N)}
        
        for i in range(N):
            # from first point
            x1, y1 = points[i]
            # all other points
            for j in range(i+1, N):
                # the point we are comparing to 
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                
                # add the point with its cost
                adj[i].append([dist, j])
                # undirected, exact opposite 
                # goes to other one
                adj[j].append([dist, i])
                
        # prim's algo
        
        res = 0
        visit = set()
        min_heap = [[0,0]] # cost, point
        
        while len(visit) < N:
            cost, i = heappop(min_heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heappush(min_heap, [nei_cost, nei])
                    
        return res
