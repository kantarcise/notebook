"""
Given the root of a binary tree, return the 
length of the diameter of the tree.

The diameter of a binary tree is the length of the
longest path between any two nodes in a tree. 

This path may or may not pass through the root.

The length of a path between two nodes is represented by
the number of edges between them.

Example 1:

    Input: root = [1,2,3,4,5]
    Output: 3

    Explanation: 
            
        3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

    Input: root = [1,2]
    Output: 1

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100

Takeaway:

    The diameter can pass through the node or not.

    For that, we need a depth calculation for the possible
    root passing solution

    We also need to calculate the diameter of the left and right
    subtrees, becuase it may be the case that max diameter is
    never passing through the root node

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree_(self, root) -> int:
        # first try
        # It works!

        # Input: root = [1,2,3,4,5]
        # 
        #          1
        #        2   3
        #      4   5
        #  
        # Output: 3
        # Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

        # if the nodes are as far as apart from each other, 
        # the will have the longest path

        if not root:
            return 0
            
        # max depth on left subtree
        d1 = self.max_depth(root.left)
        # max depth on right subtree
        d2 = self.max_depth(root.right)

        # we have to find the diameters too
        # because the diameter may not pass 
        # through from the root
        diameter1 = self.diameterOfBinaryTree_(root.left)
        diameter2  = self.diameterOfBinaryTree_(root.right)

        # Here's why these comparisons are necessary:

        # Diameter Through the Root (Combining Left and Right
        #  Subtrees):

        # The longest path in the binary tree can pass
        #  through the root. In this case, the diameter is 
        # the sum of the heights of the left and right
        #  subtrees plus 1 for the root. So, 
        # left_height + right_height + 1 is considered.

        # Diameter Within the Left Subtree:

        # The longest path may be entirely contained within
        #  the left subtree. In this case, the diameter
        #  is the diameter of the left subtree 
        # (recursively calculated).
        
        # Diameter Within the Right Subtree:

        # Similarly, the longest path may be entirely
        #  contained within the right subtree. The diameter
        #  is the diameter of the right subtree
        #  (recursively calculated).

        return max (d1 + d2, diameter1, diameter2)

    def max_depth(self, root):
        
        if root is None:
            return 0
        # we have at least 1 node
        # try left 
        d1 = self.max_depth(root.left)
        # try right
        d2 = self.max_depth(root.right)
        # 1 because we of the root
        return max(d1, d2) + 1

    def diameterOfBinaryTree(self, root) -> int:
        # neetcode approach
        # use DFS and for each node, return the diameter 
        # as well as the height
        # if a node is empty, it has -1 height for math to checkout
        # the diameter is depth of nodes + 2 (because of the edges)

        # Initialize a result list to store the maximum
        #  diameter found during DFS.
        res = [0]

        def dfs(root):
            # Base case: If the current node is None, it has a
            #  height of -1 (to facilitate calculations).
            if not root:
                return -1

            # Recursively calculate the height of the left subtree.
            left = dfs(root.left)
            # Recursively calculate the height of the right subtree.
            right = dfs(root.right)

            # Update the result with the maximum diameter found.
            # The diameter is calculated as the sum of the
            #  depths of the left and right
            #  subtrees plus 2 (accounting for the edges).
            res[0] = max(res[0], 2 + left + right)

            # Return the height of the current subtree, which
            #  is the maximum height of the left or right
            #  subtree plus 1 for the current node.
            return 1 + max(left, right)

        # Start the DFS traversal from the root node.
        dfs(root)
    
        # Return the maximum diameter found
        # during the traversal.
        return res[0]
