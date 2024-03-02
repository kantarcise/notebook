"""
There are n cities connected by some number of flights. 
You are given an array flights where 
  flights[i] = [fromi, toi, pricei] indicates that there 
  is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return 
the cheapest price from src to dst with at most k stops. 

If there is no such route, return -1.

Example 1:


Input: n = 4, 
      flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
      src = 0, dst = 3, k = 1

Output: 700
Explanation:
  
  The optimal path with at most 1 stop from city 0 to 3 is 
    marked in red and has cost 100 + 600 = 700.
  Note that the path through cities [0,1,2,3] is cheaper but 
    is invalid because it uses 2 stops.

Example 2:

Input: n = 3, 
       flights = [[0,1,100],[1,2,100],[0,2,500]], 
       src = 0, dst = 2, k = 1
Output: 200
Explanation:

  The optimal path with at most 1 stop from city 0 to 2 is 
      marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, 
      flights = [[0,1,100],[1,2,100],[0,2,500]], 
      src = 0, dst = 2, k = 0
Output: 500
Explanation:

  The optimal path with no stops from city 0 to 2 
    is marked in red and has cost 500.
 
Constraints:

  1 <= n <= 100
  0 <= flights.length <= (n * (n - 1) / 2)
  flights[i].length == 3
  0 <= fromi, toi < n
  fromi != toi
  1 <= pricei <= 10^4
  There will not be any multiple flights between two cities.
  0 <= src, dst, k < n
  src != dst

Takeaway:

  too see the graphs, 
  check: 
  https://leetcode.com/problems/cheapest-flights-within-k-stops/

  Graph traversal.

  Belmann Ford - can even deal with Negative Weights
  Dijsktra cannot do that.

"""
from collections import defaultdict
from collections import deque

class Solution:
    def findCheapestPrice_(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # does NOT WORK
        # my take
        
        adj = {src: set() for src in flights[0]}
        
        for f in flights:
            adj[f[0]].add(f[1])
            
        # go backwards from the destination
        # and check the adj map to find cities before
        # while counting the number of stops
        
        # when you find all possible routes, taken in k stops
        # compare costs and return min cost flight
        pass
        
    def findCheapestPrice__(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # my take with help
        # TIME LIMIT EXCEEDED
        
        # Make an adjacency list to represent the graph
        adj = defaultdict(list)
        for f in flights:
            adj[f[0]].append((f[1], f[2]))

        # Helper function to perform DFS
        def dfs(node, stops, cost):
            nonlocal min_cost

            # Base case: If the node is the destination
            if node == dst:
                min_cost = min(min_cost, cost)
                return

            # Base case: If the number of stops exceeds k
            if stops > k:
                return

            # Explore all neighbors
            for neighbor, price in adj[node]:
                dfs(neighbor, stops + 1, cost + price)

        # Initialize the minimum cost to infinity
        min_cost = float('inf')

        # Start DFS from the source node
        dfs(src, 0, 0)

        # Check if any valid route was found
        return min_cost if min_cost != float('inf') else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # neet
        
        # a lot of different ways to solve this one
        # Bellman-Ford method ? 
    
        # if this question did not have at most K stops,
        
        # this would be just Djikstra question
        # for calculating shortest paths, 
        # weighted or not weighted edges
    
        # we can still do it with modified Djikstra 
    
        # Or another approach is Bellman-Ford
        # We can take into account, at most k stops with Bellman-Ford
    
        # Time complexity would be - O(E * k)
        
        # Bellman Ford can even deal with Negative Weights!
        # Djikstra cannot do that.
    
        prices = [float("inf")] * n
        
        # source requires no price
        prices[src] = 0
        
        for i in range(k + 1):
            temp_prices = prices.copy()
            
            # go through every edge
            for s, d, p in flights: # source, dest, price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
            
        return -1 if prices[dst] == float("inf") else prices[dst]
    
    def findCheapestPrice___(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # from a homie 
        
        # make adj map
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # Create a queue which stores the node and their distances from the
        # source in the form of (stops, (node, dist)) with 'stops' indicating 
        # the number of nodes between src and the current node.
        q = deque([(0, (src, 0))])

        # Distance array to store the updated distances from the source.
        dist = [float('inf')] * n
        dist[src] = 0

        # Iterate through the graph using a queue like in Dijkstra with 
        # popping out the element with min stops first.
        while q:
            stops, (node, cost) = q.popleft()

            # We stop the process as soon as the limit for the stops reaches.
            if stops > K:
                continue
            
            for adjNode, edW in adj[node]:
                # We only update the queue if the new calculated dist is
                # less than the prev and the stops are also within limits.
                if cost + edW < dist[adjNode] and stops <= K:
                    dist[adjNode] = cost + edW
                    q.append((stops + 1, (adjNode, cost + edW)))

        # If the destination node is unreachable return '-1'
        # else return the calculated dist from src to dst.
        return -1 if dist[dst] == float('inf') else dist[dst]
