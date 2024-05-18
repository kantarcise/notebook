"""
Given a binary tree root and an 
integer target, delete all the leaf 
nodes with value target.

Note that once you delete a leaf node 
with value target, if its parent node 
becomes a leaf node and has the value 
target, it should also be deleted (you 
need to continue doing that until you cannot).

Example 1:

    
    Input: root = [1,2,3,2,null,2,4], target = 2
    
    Output: [1,null,3,null,4]
    
    Explanation: 
        Leaf nodes in green with value (target = 2) are
        removed. After removing, new nodes become 
        leaf nodes with value (target = 2).

Example 2:

    Input: root = [1,3,3,3,2], target = 3
    
    Output: [1,3,null,null,2]

Example 3:

    Input: root = [1,2,null,2,null,2], target = 2
    
    Output: [1]

    Explanation: 
        Leaf nodes in green with value (target = 2) 
        are removed at each step.
 
Constraints:

    The number of nodes in the tree is in the range [1, 3000].
    
    1 <= Node.val, target <= 1000

Takeaway:

    You do not have to construct the list from ground up

    as simple as possible.

"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, 
                        target: int) -> TreeNode:
        # DOES NOT WORK
        
        # STOP 
        # TRYING
        # TO MAKE
        # NEW TREES
        # FROM EMPTY
        # EVERYTIME YOU SEE 
        # A TREE QUESTION WITH SOME TRAVERSAL
        
        # we need a traversal method
        # we should delete all leaves with target val
        # we should traverse again and update the leaves
        # keep running traversal and delete until 
        # no target leave left
        
        # let's use dfs to make a leaf node list
        leaves = []
        def dfs(node,):
            if not node:
                return
            
            if not node.left and not node.right:
                # this is a leaf
                leaves.append(node.val)
                
            dfs(node.left)
            dfs(node.right)
            
        while target in set(leaves):
            dfs(root)
            # delete leaves with target
            # ???
            
        return root
    
    def removeLeafNodes_(self, root: TreeNode, 
                        target: int) -> TreeNode:
        # this works!
        
        if not root:
            return None
        
        # Recursively call removeLeafNodes 
        # on the left and right children
        root.left = self.removeLeafNodes_(root.left, target)
        root.right = self.removeLeafNodes_(root.right, target)
        
        # Check if the current node is a 
        # leaf and if its value is the target
        if (root.val == target and 
            not root.left and 
            not root.right):
            return None
        
        return root

    def removeLeafNodes(self, 
                    root: TreeNode, 
                    target: int) -> TreeNode:
        # this approach also works!
        return self.dfs(root, target)
    
    def dfs(self, root, target):
        if root is None:
            return None
        # leaf node
        if (root.val==target and 
            not root.left and 
            not root.right):
            return None
        
        root.left = self.dfs(root.left,target)
        root.right = self.dfs(root.right,target)
        
        # if node has the target as value and leaf
        if (root.val==target and 
            not root.left and 
            not root.right):
            return None
        return root
