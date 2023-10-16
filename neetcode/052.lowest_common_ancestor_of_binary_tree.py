"""
Given a binary search tree (BST), find the lowest common 
ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The
 lowest common ancestor is defined between two nodes p 
 and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself).”

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

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
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

    # this did not work
    #   doesn't handle cases where the lowest
    #   common ancestor is one of the nodes itself.
    def lowest_common_anchestor(self, root, p, q):
        # my first try
        # lets make a hashmap where we hold all ancestors 
        # for every node
        # Helper function to perform a depth-first search and 
        # record ancestors in a dictionary.
        def dfs(node, parent=None):
            if node:
                anchestors[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        # Initialize the dictionary to store ancestors.
        anchestors = {}
        # Perform DFS to populate the ancestors dictionary.
        dfs(root)

        # Initialize sets to store ancestors of p and q.
        ancestors_p = set()
        ancestors_q = set()

        # Build the set of ancestors for p.
        while p in anchestors:
            ancestors_p.add(p)
            p = anchestors[p]

        # Build the set of ancestors for q.
        while q in anchestors:
            ancestors_q.add(q)
            q = anchestors[q]

        # Find the lowest common ancestor by checking
        #  common ancestors between p and q.
        common_ancestors = ancestors_p.intersection(ancestors_q)
        return common_ancestors.pop()

    # llm approach
    def lowest_common_ancestor(self, root, p, q):
        
        def findLCA(node):
            if not node:
                return None
            # how does he know what p or q are?
            if node == p or node == q:
                return node
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            
            return None
        
        return findLCA(root)

    # neetcode
    def lowestCommonAncestor(self, root, p, q):
        
        # use the values of the nodes.
        
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


    # cool recursive approach
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If the value of p and q is greater than root, then LCA will be in the right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If one value is less and the other is greater, then root is the LCA
        else:
            return root