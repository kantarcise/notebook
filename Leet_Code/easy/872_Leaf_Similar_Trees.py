"""
Consider all the leaves of a binary tree, from left to right 
order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 
Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

Takeaway:

Classic DFS. Gotta be careful about conditions though.

Gotta think them through

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # we can make two lists 
        leaf_val_one, leaf_val_two = list(), list()
        
        def dfs(node, the_list) -> None:
            if not node.right and not node.left:
                the_list.append(node.val)
                return
            if node.left:
                dfs(node.left, the_list)
            if node.right:
                dfs(node.right, the_list)
            
        dfs(root1, leaf_val_one)
        dfs(root2, leaf_val_two)
        
        return leaf_val_one == leaf_val_two
    
    def leafSimilar_(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # from a homie
        def dfs(root):
            # If the current node is None, return an empty list
            if root is None:
                return []
          
            # Recursively explore the left and right children, and accumulate leaf values
            leaves = dfs(root.left) + dfs(root.right)
          
            # If 'leaves' is empty, it means this is a leaf node, so return its value
            # Otherwise, it means this is an internal node and 'leaves' contains its subtree's leaves
            return leaves or [root.val]

        # Compare the leaf value sequences of both trees
        return dfs(root1) == dfs(root2)
