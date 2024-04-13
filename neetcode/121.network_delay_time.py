"""
You are given a network of n nodes, labeled from 1 to n. 

You are also given times, a list of travel times as 
directed edges times[i] = (ui, vi, wi), where ui is the 
source node, vi is the target node, and wi is the time it 
takes for a signal to travel from source to target.

We will send a signal from a given node k. 

Return the minimum time it takes for all the n nodes to receive 
the signal. 

If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    
    Output: 2

Example 2:

    Input: times = [[1,2,1]], n = 2, k = 1
    
    Output: 1

Example 3:

    Input: times = [[1,2,1]], n = 2, k = 2
    
    Output: -1

Constraints:

    1 <= k <= n <= 100
    
    1 <= times.length <= 6000
    
    times[i].length == 3
    
    1 <= ui, vi <= n
    
    ui != vi
    
    0 <= wi <= 100
    
    All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Takeaway:

    Djikstra! - shortest path

    used with a set and minimum heap

    See the code!
"""

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # neet
        
        # Djikstra! - shortest path
        
        # times are directed edges. also weighted
        
        # how long will it take to get the singal by everyone?
        
        # from the example
        # weights are in paranthesis () - brackets [] - braces {}
        
        #          2
        #     (1)/   \(1) 
        #       1     3
        #            /(1)
        #           4
        
        # how long will it take? 2
        # because from 2 to 4, road is 2, 
        # and 2 is max time
        
        # Djikstra is kinda like a BFS, wth a min_Heap
        # which will hold (path_cost, node)
        
        # start with pushing starting node to heap
        # pop it and go the first layer from the node
        
        
        #     1
        #     |\
        #  (1)| \ (4)
        #     |  \ 
        #     3   2
        #      \  |
        #   (1) \ | (1)
        #        \| 
        #         4
        
        # for this example, min heap will look like this
        
        #         min_heap
        #  _________________
        #  |  path , node   |
        #  ------------------
        #  |  (0)  ,   1    |  # start from top left
        #  ------------------
        #  |  (1)  ,   3    |  # first layer, we will pop
        #  |  (4)  ,   2    |  #       based on min path 
        #  -----------------   
        #  |  (2)  ,   4    |  -- from node 3 to 4
        #  -----------------   # path is (2) for node 4 beacuse
        #  |  (3)  ,   2    |      # we want to know the path 
                                    # from starting point, node 1
                
        # although node 2 is added to our min_heap
        # when we take the path coming from node 4
        # we have a smaller path!
        
        # we have a value left in our heap (4), 2
        # but we covered that path anyway so we are good
        
        # time complexity is o(E log V)
        # number of edges = V^2
        # the size of min_heap is V^2
        # which we will pop from in log time, for E edges
        # this results to O(E log (V^2)) = O(2E log(V)) = O(E log V)
        
        edges = defaultdict(list)
        
        # make the adjacency list
        for u,v,w in times:
            # get every outgoing neighbour
            edges[u].append((v, w))
            
        min_heap = [(0, k)]
        visit = set()
        t = 0
        while min_heap:
            w1, n1 = heappop(min_heap)
            
            if n1 in visit:
                continue
                
            visit.add(n1)
            # the weight we just got - w1
            t = max(t, w1)
            
            # bfs
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # add the new path as added
                    heappush(min_heap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
