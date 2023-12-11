"""

Given the root of a binary tree and an integer targetSum, return true 
if the tree has a root-to-leaf path such that adding up all the values 
along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Takeaway:

Classic DFS
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        all_sums = set()
        def dfs(node, current_sum):
            # if the Node is None
            if not node:
                return
            
            current_sum += node.val
            
            # no children
            if not (node.left or node.right):
                all_sums.add(current_sum)
                return 
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
        dfs(root, 0)
        return targetSum in all_sums
