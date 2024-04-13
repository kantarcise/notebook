"""
Given the root of a binary tree, imagine yourself standing 
on the right side of it, return the values of the nodes 
you can see ordered from top to bottom.

Example 1:

    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

Example 2:

    Input: root = [1,null,3]
    Output: [1,3]

Example 3:

    Input: root = []
    Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Takeaway:

    Only going right won't work

    The nodes on the left subtree can still have some right nodes
    that should have been taken into account

    We can use Breadth First Search - Level Ordering Traversal

    At each level, we will be searching for the right most node

    Loop through all the nodes at the current level. 
    For each node, remove it from the left end of 
    the deque (q) using q.popleft().

    If the node is not None, update right_side to 
    the current node. This is because you are traversing 
    from left to right within the level, so the rightmost 
    node encountered will be the last one 
    assigned to right_side.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rightSideView_(self, root: "TreeNode") -> "list[int]":
        # first approach
        # starting from the node, only go to the right nodes.
        # return a list of those node values

        # THIS DOES NOT WORK

        result = []

        def dfs_right(node):
            if not node:
                return
            result.append(node.val)
            dfs_right(node.right)

        dfs_right(root)

        return result 

    def rightSideView(self, root: "TreeNode") -> "list[int]":
        
        # lets use BFS
        result = []

        # we bfs we use a deque
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            right_side = None

            for _ in range(length):
                # Loop through all the nodes at the current level. 
                # For each node, remove it from the left end of 
                # the deque (q) using q.popleft().

                # If the node is not None, update right_side to 
                # the current node. This is because you are traversing 
                # from left to right within the level, so the rightmost 
                # node encountered will be the last one 
                # assigned to right_side.
                node = q.popleft()
                if node:
                    right_side = node
                    # these could be None but thats fine
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                # right side is not None
                result.append(right_side.val)
        
        return result
