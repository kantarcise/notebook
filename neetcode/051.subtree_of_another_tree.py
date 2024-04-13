"""
Given the roots of two binary trees root and subRoot
return True if there is a subtree of root with
the same structure and node values of subRoot and
False otherwise.

A subtree of a binary tree tree is a tree that 
consists of a node in tree and all of this node's 
descendants. The tree tree could also be considered as 
a subtree of itself.

Example 1:

    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -10^4 <= root.val <= 10^4
    -10^4 <= subRoot.val <= 10^4

Takeaway:

    The brute force algorithm will run in O(s * t)

    Most tree problems are easier when we think recursively.

    However, do not forget the edge cases.

    We basically just write the same_tree method and use it 
    in our is_subtree method

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
      
    def isSubtree_(self, root, subRoot):
        # We want to traverse the tree and check if there 
        # is same tree within it

        # Helper function to check if two trees are the same.
        def same_tree(s, q):
            if not s and not q:
                return True
            if not s or not q:
                return False
            
            # check both sides and nodes themselves
            return s.val == q.val and same_tree(s.left, q.left) and same_tree(s.right, q.right)

        # Base case: If the current node of the root tree is None, return False.
        if not root:
            return False

        # Check if the current subtree rooted at the current node matches the subRoot tree.
        if same_tree(root, subRoot):
            return True

        # If not, recursively check the left and right subtrees of the root tree.
        return self.isSubtree_(root.left, subRoot) or self.isSubtree_(root.right, subRoot)


    def isSubtree(self, root, subRoot) -> bool:
        # another approach would be to have an seperate method within the class.

        # if tree subRoot is None, return True
        if not subRoot:
            return True

        # if root is None and subroot is not None, return False
        if not root and subRoot: 
            return False        

        # both of the trees are not empty
        if self.sameTree(root, subRoot):
            return True

        # check if the subTree is a subtree of root
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sameTree(self, s, t):
        # if both trees are None
        if not s and not t:
            return True
        
        # if both trees are not None and they have same values
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        
        # if one of them is empty and the other is not
        return False

        
