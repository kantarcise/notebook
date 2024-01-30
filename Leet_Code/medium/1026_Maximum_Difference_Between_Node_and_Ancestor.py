"""
Given the root of a binary tree, find the maximum value v for 
which there exist different nodes a and b 
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is 
equal to b or any child of a is an ancestor of b.

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

Takeaway:

Traverse with DFS, update the max difference.

"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # made with tips from senior engineer
        
        # we can traverse the tree with dfs,
        # while updating max difference
        
        def dfs_diff(node, min_val, max_val):
            if not node:
                return max_val - min_val
            
            # Update min and max values at each node
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            
            # Recursively calculate the maximum difference 
            # for left and right children
            left_diff = dfs_diff(node.left, min_val, max_val)
            right_diff = dfs_diff(node.right, min_val, max_val)
            
            # Return the maximum difference among the left, right, and current node
            return max(left_diff, right_diff, max_val - min_val)

        # Call the DFS function with the root and initial min and max values
        return dfs_diff(root, root.val, root.val)
