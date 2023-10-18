"""
Given the root of a binary tree, determine if 
it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes 
with keys less than the node's key.

The right subtree of a node contains only 
nodes with keys greater than the node's key.

Both the left and right subtrees must 
also be binary search trees.
 
Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

Takeaway: 

you can think "this is dfs, just check neighbors"
that does not cut it.

       5
   3       7
          4  8

the 4 in the tree is not recogniziable just with checking neighbors  

as we go down the tree, we need to update boundaries

as we go to left, we need to update right boundary
as we go to right, we need to update left boundary

so that we have a binary search tree      
        
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def isValidBST(self, root: "TreeNode") -> bool:
        # first try
        #  there are a few issues in your implementation:

        # You should return False as soon as you encounter 
        # a violation of the BST property, rather than returning 
        # result * 0. Multiplying by zero doesn't give the desired 
        # effect for error-checking.
        # 
        # The result variable isn't correctly propagated 
        # through the recursive calls.
        # 
        # You're not considering the entire subtree 
        # when checking if it's a valid BST.

        def dfs(node, result):
            if not node:
                return result
            
            # stop cheking the level deeper
            # focus on your current level
            if node.left:
                if node.left.val <= node.val:
                    result *= 1
                else:
                    result *= 0
           
            if node.right:
                if node.right.val >= node.val:
                    result *= 1
                else:
                    result *= 0
            dfs(node.left, result)
            dfs(node.right, result)

            return result

        return dfs(root, 1)

    # llm
    def isValidBST(self, root: "TreeNode") -> bool:
        
        
        def is_valid_bst(node, min_val = float("-inf") , max_val =  float("inf")):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return (is_valid_bst(node.left, min_val, node.val) and 
                    is_valid_bst(node.right, node.val, max_val))

        return is_valid_bst(root)

    def isValidBst(root, min_val, max_val):
        
        # you can think "this is dfs, just check neighbors"
        # that does not cut it.

        #        5
        #    3       7
        #           4  8

        # the 4 in the tree is not recogniziable just with checking neighbors  

        # as we go down the tree, we need to update boundaries
        # as we go to left, we need to update right boundary
        # as we go to right, we need to update left boundary
        # so that we have a binary search tree      
        
        def valid(node, left_bound, right_bound):
            if not node:
                return True

            if not (node.val < right_bound and node.val > left_bound):
                return False

            return (valid(node.left, left_bound, node.val) and 
                    valid(node.right, node.val, right_bound))

        return valid(root, float("-inf"), float("inf"))