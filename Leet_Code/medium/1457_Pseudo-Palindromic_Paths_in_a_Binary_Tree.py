"""
Given a binary tree where node values are digits from 1 to 9. 

A path in the binary tree is said to be pseudo-palindromic if at 
least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from 
the root node to leaf nodes.

Example 1:

    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    
    Explanation: 
        
        There are three paths going from the root node to 
            leaf nodes: the red path [2,3,3], the green path [2,1,1], 
            and the path [2,3,1]. 
            
        Among these paths only red path and green path are pseudo-palindromic 
        paths since the red path [2,3,3] can be rearranged 
        in [3,2,3] (palindrome) and the green path [2,1,1] can 
        be rearranged in [1,2,1] (palindrome).

Example 2:

    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    
    Explanation: 
        There are three paths going from the root node to leaf 
        nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. 
        
        Among these paths only the green path is pseudo-palindromic 
        since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

    Input: root = [9]
    Output: 1

Constraints:

    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9

Takeaway:

    DFS.
  
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def dfs(node, path_count):
            if not node:
                return
            
            # Update the count for the current node's value in the path
            path_count[node.val] = path_count.get(node.val, 0) + 1
            
            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                odd_count = 0
                for count in path_count.values():
                    if count % 2 == 1:
                        odd_count += 1
                if odd_count <= 1:
                    self.count += 1
            
            # Recursively traverse the left and right subtrees
            dfs(node.left, path_count.copy())
            dfs(node.right, path_count.copy())
        
        dfs(root, {})
        return self.count
