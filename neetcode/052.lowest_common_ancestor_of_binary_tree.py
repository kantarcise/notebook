"""
Given a binary search tree (BST), find the lowest common 
ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 

“The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where 
we allow a node to be a descendant of itself).”

Example 1:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    
    Explanation: The LCA of nodes 2 and 4 is 2, since a node is always
    can be a descendant of itself according to the LCA definition.

Example 3:

    Input: root = [2,1], p = 2, q = 1
    Output: 2
 
Constraints:

    The number of nodes in the tree is in the range [2, 10^5].
    
    -10^9 <= Node.val <= 10^9
    
    All Node.val are unique.
    
    p != q
    
    p and q will exist in the BST.

Takeaway:

    Its a binary search tree so the values are really useful.

    if both of the values are smaller than root.val
    go to left subtree

    if both of the values are larger than root.val
    go to right subtree

    if one is bigger and one is smaller than root.val
    the anchestor will be the split happens in the tree
    the LCA is found, so to speak

    If we bump into the node, starting from the the root
    that is the LCA because nothing below will be 
    the common ancestor 

    time complexity is the height of the tree, o(log n)
    because we are only visiting single node at each level

    We can also approach the question recursively

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor__(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # llm approach
        
        def findLCA(node):
            if not node:
                return None
            
            # if the node is one of p or q, we found the answer!
            if node == p or node == q:
                return node
            
            # recur on left and right
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            # if they both returned a node
            if left and right:
                return node
            
            # if only left or right returned
            if left:
                return left
            
            if right:
                return right
            
            # None of them returned
            return None
        
        return findLCA(root)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # use the values of the nodes.
        # this is way faster

        # if both of the values are smaller than root.val
        # go to left subtree
        
        # if both of the values are larger than root.val
        # go to right subtree

        # if one is bigger and one is smaller than root.val
        # the anchestor will be the split happens in the tree
        # the LCA is found, so to speak

        # If we bump into the node, starting from the the root
        # that is the LCA because nothing below will be 
        # the common ancestor

        # time complexity is the height of the tree, o(log n)
        # because we are only visiting single node at each level

        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                # go to right subtree
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current


    def lowestCommonAncestor__(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # cool recursive approach
        # explicitly calling the method ourselves

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor__(root.left, p, q)
        # If the value of p and q is greater than root, then LCA will be in the right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor__(root.right, p, q)
        # If one value is less and the other is greater, then root is the LCA
        else:
            return root
