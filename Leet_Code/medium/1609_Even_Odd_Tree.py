"""
A binary tree is named Even-Odd if it meets 
the following conditions:

    The root of the binary tree is at level index 0, its 
  children are at level index 1, their children 
  are at level index 2, etc.

    For every even-indexed level, all nodes at the level 
  have odd integer values in strictly increasing 
  order (from left to right).

    For every odd-indexed level, all nodes at the 
  level have even integer values in strictly 
  decreasing order (from left to right).

    Given the root of a binary tree, return true if 
  the binary tree is Even-Odd, otherwise 
  return false.

Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and 
levels 1 and 3 are all even and decreasing, the 
tree is Even-Odd.

Example 2:

Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly 
increasing order, so the tree is not Even-Odd.

Example 3:

Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 
should be even integers.
 
Constraints:

  The number of nodes in the tree is in the range [1, 105].
  1 <= Node.val <= 106

Takeaway:

  BFS to the rescue!

  We can decide the result while we are traversing.

"""

from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # this solution works, but not very fast
        
        def strictly_increasing(L):
            return all(x<y for x, y in zip(L, L[1:]))

        def strictly_decreasing(L):
            return all(x>y for x, y in zip(L, L[1:]))
        
        
        # we can use breadth first search
        q = deque()
        level_map = defaultdict(list)
        level = 0
        
        q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()            
                level_map[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
                
        # print(level_map)
        for k, v in level_map.items():
            if k % 2 == 0:
                # all odd, increasing
                for elem in list(v):
                    if elem % 2 == 0:
                        return False
                if not strictly_increasing(list(v)):    
                    return False
            else:
                # all even, decreasing
                for elem in list(v):
                    if elem % 2 != 0:
                        return False
                if not strictly_decreasing(list(v)):    
                    return False
                
        return True
    
    def isEvenOddTree_(self, root: Optional[TreeNode]) -> bool:

        # This solution seems to be faster
        # we can decide while we are traversing

        queue = deque([root])

        level = 0

        while queue:
            if level % 2 == 0:
                lastVal = 0
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.val % 2 == 0:
                        return False
                    
                    if node.val <= lastVal:
                        return False
                    
                    lastVal = node.val
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)


            else:
                lastVal = inf
                for _ in range(len(queue)):
                    node = queue.popleft()
                    
                    if node.val % 2 != 0:
                        return False
                    
                    if node.val >= lastVal:
                        return False
                    
                    lastVal = node.val
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                        
            level += 1
                
        return True      
