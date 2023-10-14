"""
Given a binary tree, determine if it is height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
 
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

Takeaway:

We can do a recursive DFS on subtrees and compare the results
This will be o(n) * n

We can use the heights of the subtrees and return a boolean 
based on not expecting a node height

``` return height != -1```

We can do better than starting from root node and asking the question
is the subtree balanced ? again and again

Just define a recursive dfs but alongside balance, return the height too

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def is_balanced(self, root) -> bool:
        # first try
        # the height difference between subtrees 
        # have to be at most 1
        
        def return_max_depth(root):
            pass
        
        return True if return_max_depth(root.left) - return_max_depth(root.right) > 1 else False
    
    def is_balanced(self, root) -> bool:
        # llm approach, same idea as mine
        # Helper function to calculate the height of a tree.
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            # Check if the subtree is balanced, and if not, return -1.
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            # Return the height of the subtree.
            return 1 + max(left_height, right_height)

        # Call the helper function for the root of the tree.
        height = get_height(root)

        # If the height is -1, the tree is unbalanced; otherwise, it's balanced.
        return height != -1


    def isBalanced(self, root) -> bool:
        
        # not even faster than my approach
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
        
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]