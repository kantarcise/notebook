"""
You are given the root of a binary tree containing 
digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents 
the number 123.

Return the total sum of all root-to-leaf numbers. 

Test cases are generated so that the answer will 
fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

    Input: root = [1,2,3]
    
    Output: 25
    
    Explanation:
        
        The root-to-leaf path 1->2 represents the number 12.
        The root-to-leaf path 1->3 represents the number 13.
        Therefore, sum = 12 + 13 = 25.

Example 2:

    Input: root = [4,9,0,5,1]
    
    Output: 1026
    
    Explanation:
        
        The root-to-leaf path 4->9->5 represents the number 495.
        The root-to-leaf path 4->9->1 represents the number 491.
        The root-to-leaf path 4->0 represents the number 40.
        Therefore, sum = 495 + 491 + 40 = 1026.
 
Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    
    0 <= Node.val <= 9
    
    The depth of the tree will not exceed 10.

Takeaway:

    Filling a list while traversing through DFS is pretty normal.

    You do your computation before recursion and after base case.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # run until you find a leaf
        # add current path into total
        
        # Initialize variables to store the 
        # total sum and the current path
        result = []
        
        def dfs(node, path):
            # base case
            if not node:
                return
            
            # Add the current node's value to the path
            # 1 becomes 12 or 13
            path = path * 10 + node.val
            
            # If it's a leaf node, add the 
            # complete path to the result
            if not node.left and not node.right:
                result.append(path)
                return
            
            # Continue DFS traversal
            dfs(node.left, path)
            dfs(node.right, path)
        
        # Start DFS traversal from the root with an initial path of 0
        dfs(root, 0)
        
        # Return the sum of all root-to-leaf numbers
        return sum(result)
