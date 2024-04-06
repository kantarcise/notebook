"""
Given the root of a binary tree, invert the
tree, and return its root.

Example 1:

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:

    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:

    Input: root = []
    Output: []
 
Constraints:

    The number of nodes in the tree is in the range [0, 100].

    -100 <= Node.val <= 100

Takeaway:

    We can approach the problem with recursion

    Simply make the swap and call the method on to the children Node

    Depth-First Search (DFS) in the context of a binary tree:
     
    DFS is a common algorithm used for traversing or searching tree and 
    graph data structures. In this specific case, it's a pre-order
    DFS because it visits the current node, then recursively explores
    its left and right subtrees.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def invertTree_(self, root):
        # my first try
        # the approach was somewhat correct
        # does not work though
        
        # how do we invert a tree?
        # it it has a child, we should be switching it's children.
        # if it's a leaf, dont do anything
        
        current = root
        if current.left == None and current.right == None:
            return  
        while current.left != None and current.right != None:
            temp = current.left
            current.left = current.right
            current.right = temp         

        return current

    def invertTree(self, root):
        if root is None:
            return None

        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
