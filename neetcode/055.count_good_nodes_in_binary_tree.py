"""
Given a binary tree root, a node X in the tree is 
named good if in the path from root to X there are no 
nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4

Explanation: Nodes in blue are good.

Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting 
from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" 
is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

Takeaway:

YOu dont have to pass the whole path to the lower level
you just need to pass the max value
        
We can use preorder traversal (dfs)

Root is always a good node and root is equal to root

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def good_nodes(self, root: "TreeNode") -> int:
        # first try with help of LLM

        # we need a mechanism to hold every path
        #  for each node in the tree
        # so that we can compare parents to children
        # no we don't. Thats too complex
        # good_nodes = [root]
        # 
        # node_and_path = {root: [None]}

        # visit every node in the tree
        # and compare parents to children

        def dfs(node, max_val):
            if not node:
                return 0  # No good nodes in this subtree

            good_count = 0

            if node.val >= max_val:
                good_count = 1

            # update the max value
            max_val = max(max_val, node.val)

            # call dfs on deeper level
            # left subtree
            left_count = dfs(node.left, max_val)
            # right subtree
            right_count = dfs(node.right, max_val)

            return good_count + left_count + right_count

        return dfs(root, float("-inf"))
    
    # neetcode
    def goodNodes(self, root: "TreeNode") -> int:
        
        # preorder traversal
        # dfs
        # pass the greatest value to the subtree
        # NOT all the values we have seen so far.
        # there is no need to do that.
        
        # result = 1 + left + right

        def dfs(node, max_value):
            
            if not node:
                return 0

            result = 1 if node.val >= max_value else 0

            max_value = max(max_value, node.val)
            result += dfs(node.left, max_value)
            result += dfs(node.right, max_value)

            return result

        return dfs(root, root.val)