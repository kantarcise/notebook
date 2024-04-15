"""
Given the root of a binary tree, return the 
inorder traversal of its nodes' values.

Example 1:

    Input: root = [1,null,2,3]
    
    Output: [1,3,2]

Example 2:

    Input: root = []
    
    Output: []

Example 3:

    Input: root = [1]
    
    Output: [1]

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    
    -100 <= Node.val <= 100
 
Follow up: 

    Recursive solution is trivial, could you do it iteratively?

Takeaway:

    DFS to traverse the tree! 

    How are you going to get the result as you traverse?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        # we can simply use dfs for it.

        # the result which we will populate
        result = []

        def dfs(node):
            # if node is None, just return
            if not node:
                return
            
            # go toward the left most element
            dfs(node.left)
            
            # after you cannot, you can append 
            # element to result
            result.append(node.val)
            
            # go right after
            dfs(node.right)

        # call dfs on root
        dfs(root)
        return result