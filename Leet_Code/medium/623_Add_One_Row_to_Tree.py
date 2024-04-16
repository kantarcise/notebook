"""
Given the root of a binary tree and two integers val 
and depth, add a row of nodes with value val at 
the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree 
        node cur at the depth depth - 1, create two tree 
        nodes with value val as cur's left subtree root 
        and right subtree root.
    
    cur's original left subtree should be the left 
        subtree of the new left subtree root.
    
    cur's original right subtree should be the right 
        subtree of the new right subtree root.
    
    If depth == 1 that means there is no depth depth - 1 
        at all, then create a tree node with value val as 
        the new root of the whole original tree, and the 
        original tree is the new root's left subtree.
 
Example 1:

    Input: root = [4,2,6,3,1,5], val = 1, depth = 2
    
    Output: [4,1,1,2,null,null,6,3,1,5]
    
Example 2:

    Input: root = [4,2,null,3,1], val = 1, depth = 3
    
    Output: [4,2,null,1,1,3,null,null,1]

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    
    The depth of the tree is in the range [1, 10^4].
    
    -100 <= Node.val <= 100
    
    -10^5 <= val <= 10^5
    
    1 <= depth <= the depth of tree + 1

Takeaway:

    BFS naturally, we need a deque for it.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        # If depth is 1, make a new root and 
        # set the original tree as its left subtree
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        # Use BFS to traverse the tree 
        # up to the depth-1 level
        level = 1
        
        # keep node as well as it's level in deque
        queue = deque([(root, level)])
        
        while queue:
            node, level = queue.popleft()
            if level == depth - 1:
                # the condition we are looking for

                # Insert new nodes as left and right children 
                # of the current node at depth-1
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                
                # make connections
                # new node can reach the down level
                new_left.left = node.left
                new_right.right = node.right
                
                # now the left and right
                # are the new nodes we've made
                node.left = new_left
                node.right = new_right
            else:
                # traverse the tree regularly
                # with just updates on level
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return root
