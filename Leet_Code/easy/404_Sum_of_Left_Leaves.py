"""
Given the root of a binary tree, return the sum of 
all left leaves.

A leaf is a node with no children. 

A left leaf is a leaf that is the left child of another node.

Example 1:

    Input: root = [3,9,20,null,null,15,7]
    
    Output: 24

    Explanation: 
        There are two left leaves in the binary 
       tree, with values 9 and 15 respectively.


Example 2:

    Input: root = [1]
    
    Output: 0

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    
    -1000 <= Node.val <= 1000
    
Takeaway:

    BFS - queues, conditions, popping and appending to the queue

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # if there are no nodes
        if not root:
            return 0
        
        # we use a deque to hold nodes at every level
        # (node, is_left)
        queue = deque([(root, False)])
        
        # result initially
        total_sum = 0
        
        while queue:
            # pop from left
            node, is_left = queue.popleft()
            
            # check conditions
            if is_left and not node.left and not node.right:
                # this is a leaf!
                total_sum += node.val
            
            # add children to queue
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        
        return total_sum
