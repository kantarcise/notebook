"""
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary 
tree and inorder is the inorder traversal of the same 
tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

Takeaway:

Reminder on traversals:

preorder traversal
starts from root, and its just like reading

inorder traversal
slide from left to right
        
after from seperating the root from preorder traversal
we will use inorder traversal tom determine
which of the nodes should be in the right subtree and
which should be in the left subtree

in order 
it will give us for every node 
which nodes are on its left and which are on its right

the left subtree is where we start from 1 in preorder until mid
and left side in inorder traversal 
``` root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid]) ```
the right subtree is where we start from mid + 1 in preorder until end
and right side in inorder traversal 
``` root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) ```
 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def buildTree(self, preorder: "list[int]", inorder : "list[int]") -> "TreeNode":
        # first try        
        # we can use the inorder traversal to 
    
        root_value = preorder[0]

        def inverse_dfs(node):
            pass

        inverse_dfs()

        pass

    # neetcode
    def buildTree(self, preorder: "list[int]", inorder : "list[int]") -> "TreeNode":
        # preorder traversal
        # starts from root, and its just like reading

        # inorder traversal
        # slide from left to right
        
        # after from seperating the root from preorder traversal
        # we will use inorder traversal tom determine
        # which of the nodes should be in the right subtree and
        # which should be in the left subtree

        # in order 
        # it will give us for every node 
        # which nodes are on its left and which are on its right

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        # mid from the inorder traversal
        mid = inorder.index(preorder[0])
        
        # the left subtree is where we start from 1 in preorder until mid
        # and left side in inorder traversal 
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])
        # the right subtree is where we start from mid + 1 in preorder until end
        # and right side in inorder traversal 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])  
        return root 