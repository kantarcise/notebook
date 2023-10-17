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

use breadth-first search. We use queues for that.

Initialize the queue with the root node

For each level, make a list of nodes
move on to (possibly) existing child nodes

"""

from collections import deque

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # llm approach sprinkled on mine
    # honestly more simple solution
    def level_order(self, root: "TreeNode") -> "list[list[int]]":
        # lets use breadth-first search

        # simple edge case        
        if not root:
            return []

        result = []
        deq = deque()
        # Initialize the queue with the root node
        deq.append(root)  

        while deq:
            # for that level
            level_vals = []
            level_size = len(deq)

            for _ in range(level_size):
                current = deq.popleft()
                # add to level value list
                level_vals.append(current.val)

                # check if current has left / right nodes
                if current.left:
                    deq.append(current.left)
                if current.right:
                    deq.append(current.right)

            result.append(level_vals)
        return result

    def levelOrder(self, root: "TreeNode") -> "list[list[int]]":
        # for each level, add all elements in the queue
        # when you are left with empty queue,
        # you can move on to the next level
        result = []
        q = deque()
        q.append(root)

        while q:
            length_of_q = len(q)
            level = []
            for i in range(length_of_q):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result