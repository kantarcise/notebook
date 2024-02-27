"""
Given the root of a binary tree, return the 
length of the diameter of the tree.

The diameter of a binary tree is the length of the 
longest path between any two nodes in a tree. This path 
may or may not pass through the root.

The length of a path between two nodes is 
represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

Constraints:

  The number of nodes in the tree is in the range [1, 104].
  -100 <= Node.val <= 100

Takeaway:

  A classic DFS.
  Using an instance variable might be solid.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree_(self, root: Optional[TreeNode]) -> int:
        # Does not work
        # because we are putting the cart before the horse
        # we can add the two of longest paths on left and right
        
        def dfs(node, path_length):
                
            # if no node
            if not node:
                return path_length
            
            biggest_path = max(dfs(node.right, path_length + 1),
                               dfs(node.left, path_length + 1))
            return biggest_path
            
        return dfs(root.left, 0) + dfs(root.right, 0) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # update diameter if the path through the current node is longer
            self.diameter = max(self.diameter, left_height + right_height)
            
            # return the height of the subtree rooted at the current node
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter
