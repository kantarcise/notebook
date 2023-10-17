"""
Given the root of a binary tree, return the level 
order traversal of its nodes' values. (i.e., from 
left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

Takeaway:

"""

# Definition for a binary tree node.
from time import thread_time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def levelOrder(self, root: "TreeNode") -> "list[list[int]]":
        # we can use a breadth first search here with a queue

        result = []

        current = root

        def bfs(node):
            if current == None:
                pass 

            bfs(thread_time)

        bfs(root)

        return result