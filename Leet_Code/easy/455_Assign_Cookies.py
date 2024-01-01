"""
Assume you are an awesome parent and want to give your children 
some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a 
cookie that the child will be content with; and each cookie j has a 
size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, 
and the child i will be content. Your goal is to maximize the number 
of your content children and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1

Takeaway:

Both heaps and sorting is cool approaches.

"""

from heapq import heapify, heappop

class Solution:
    def findContentChildren__(self, g: List[int], s: List[int]) -> int:
        # this solution does not work
        # greed and size lists
        heapify(s)
        heapify(g)
        content = 0
        
        while s and g:
            
            if heappop(s) >= heappop(g):
                content +=1
            else:
                pass
        return content
        
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(s)
        heapify(g)
        content = 0
        
        while g and s:
            p = heappop(s)
            # compare popped value from s to g
            if p >= g[0]:
                heappop(g)
                content += 1
            # if that cookie is no match for anyone, it is not useful anyway
        return content
    
    def findContentChildren_(self, g, s) -> int:
        # sorted solution from a homie
        g.sort()
        s.sort()
        count = 0

        while g:
            if s:
                if s[-1] >= g[-1]:
                    s.pop()
                    g.pop()
                    count += 1
                else:
                    g.pop()
            else:
                break
            
        return count
