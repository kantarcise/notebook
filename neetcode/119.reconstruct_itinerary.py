"""
You are given a list of airline tickets where 

    tickets[i] = [from_i, to_i] 

represent the departure and the arrival airports of one flight. 

Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the 
itinerary must begin with "JFK". 

If there are multiple valid itineraries, you should return the 
itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller 
lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. 

You must use all the tickets once and only once.

Example 1:

    Input: tickets = [["MUC","LHR"],
                      ["JFK","MUC"],
                      ["SFO","SJC"],
                      ["LHR","SFO"]]

    Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:

    Input: tickets = [["JFK","SFO"],
                      ["JFK","ATL"],
                      ["SFO","ATL"],
                      ["ATL","JFK"],
                      ["ATL","SFO"]]

    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

    Explanation: Another possible reconstruction 
                    is ["JFK","SFO","ATL","JFK","ATL","SFO"] 
                    but it is larger in lexical order.

Constraints:

    1 <= tickets.length <= 300
    
    tickets[i].length == 2
    
    from_i.length == 3
    
    to_i.length == 3
    
    from_i and to_i consist of uppercase English letters.
    
    from_i != to_i

Takeaway:

    itinerary means flight history.

    Make an adjacency list with {}, sort it!

    adj = {source: [destination1, destination2]} ..

    done when len(result) == len(tickets) + 1

    we sometimes had to backtrack, because we migth not
    be able to come back from a one way edge

"""
from heapq import heapify, heappop
from collections import defaultdict

class Solution:
	
    def findItinerary_(self, tickets: list[list[str]]) -> list[str]:
        # great solution, TIME LIMIT EXCEEDED
        
        # itinerary means flight history.
        
        # return the smallest lexical order
        # we have to use every ticket once
        
        # if we had no loops, this was a simple dfs problem, 
        # starting from JFK
        
        # we are goind to make a adjacency list with a map
        
        # adj = {source: [destination1, destination2]}
        
        # this adjaceny list should be sorted, and for that we need 
        
        # tickets to be in order, double sorted wrt first and second 
        # element within tickets
        
        # as we traverse the graph, we should remove elements 
        # from our adjacency list
        
        # we are done when len(result) == len(tickets) + 1
        
        # we sometimes had to backtrack, because we migth not
        # be able to come back from a one way edge
        
        adj = {src : [] for src, dst in tickets}
        
        tickets.sort()
        
        for src, dst in tickets:
            adj[src].append(dst)
            
        # always
        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                # a valid path found
                return True
            if src not in adj:
                # if this source has 
                # no outgoing edges
                return False
            
            temp = list(adj[src])
            
            for i, v in enumerate(temp):
                adj[src].pop(i)
                # this is our current path
                res.append(v)
                # if dfs returns True for this path
                if dfs(v): return True
                
                # if it does not, we have to backtrack
                adj[src].insert(i,v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
                
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # from a homie - works!
        
        # each ticket maps to one source <-> destination flight
        src_dest_dict = defaultdict(list)
        
        # update fly map
        for src, dst in tickets:    
            src_dest_dict[src].append(dst)

		# keep fly map with lexical order in minHeap
        for airport in src_dest_dict:
            heapify( src_dest_dict[airport] )
        
        # record of traversal path
        traverse_stack = []

        def dfs(fly_map, airport):
            
            # Exhaust all elems 
            while src_dest_dict[airport]:
                dest = heappop( src_dest_dict[airport] )
                dfs(fly_map, dest)

            traverse_stack.append(airport)
            
        # Start from JFK with all ticket used 
        # exactly once (i.e., all edges visited exactly once)
        dfs(fly_map = src_dest_dict, airport = "JFK")
        
        # print(traverse_stack)
        # print(traverse_stack.sort(reverse = True))
        
        # for a reason, these do not work
        # traverse_stack.sort()
        
        # return traverse_stack 
        return [*reversed(traverse_stack)]
