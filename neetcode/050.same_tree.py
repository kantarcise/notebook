"""
Given the roots of two binary trees p and q, write a function
to check if they are the same or not.

Two binary trees are considered the same if they are
 structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

Takeaway:

My approach was to traverse the tree and add all elements together

We can use DFS - 
with time complexity o(p+q) - all elements in both trees

Make a recursive call on the children of the node 
you are working on

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def is_same_tree(self, p, q ) -> bool:
        # first try
        # the preorder traversal of same trees should be the same
        def preorder_traversal(root):
            if not root:
                return ["_"]
            return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

        return preorder_traversal(q) == preorder_traversal(p)

    
    def isSameTree(self, p, q) -> bool:
        
        # base cases for recursive method
        # both None
        if not p and not q:
            return True
        # only one of them is None
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        # now the recursive step
        return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        