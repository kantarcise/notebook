"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

Takeaway:

My natural approach was to just recursive DFS 

3 ways to solve it: Recursive DFS, Iterative DFS and Breadth-First Search

Recursively calculate the depth and return the maximum among them

If you want no recursion, BFS is cool. You can use a queue to hol the nodes 
and increase depth on each level

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # first try
    def max_depth(self, root):
        
        if root is None:
            return 0
        # we have at least 1 node
        # try left 
        d1 = self.max_depth(root.left)
        # try right
        d2 = self.max_depth(root.right)
        # 1 because we of the root
        return max(d1, d2) + 1

    # neetcode approach 
    # recursive DFS      
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # without recursion
    # BFS
    # We learned that making BFS involves a Queue
    def maxDepthIterativeBFS(self, root) -> int:

        if not root:
            return 0

        level = 0
        # for BFS
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                # Starts from root
                node = queue.popleft()  
                # add all children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level      

    def maxDepthIterativeDFS(self, root) -> int:
        # preorder approach with a stack
        # stack holds all nodes as well as their depth
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop() 
            
            # if root is None, this will pass, result is just 0
            if node:
                # if not, compare the depth with current result
                result = max(result, depth)
                # add the children to the stack
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result