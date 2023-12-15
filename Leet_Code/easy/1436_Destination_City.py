"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a 
direct path going from cityAi to cityBi. Return the destination city, that is, the 
city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any 
loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city 
which is the destination city. 

Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.

Takeaway:

You learned about Data Structures and Algorithms. Use them.

Using a set is key.

Calm down and understand the question. How can you get to the answer?

"""

class Solution:
            
    def destCity___(self, paths: List[List[str]]) -> str:
        # use DS AND ALG YOU LEARNED IT FOR A REASON    
        source, dest=zip(*paths)        
        return (set(dest)-set(source)).pop()
    
    def destCity__(self, paths):
        # one liner
        return ({dest for _, dest in paths} - {depar for depar, _ in paths}).pop()
        
    def destCity(self, paths: List[List[str]]) -> str:
        # all starting points
        s=set(p[0] for p in paths)
        # if a destination is not around starting points
        for path in paths:
            if path[1] not in s:
                return path[1]
