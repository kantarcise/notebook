"""

Given the roots of two binary trees root and
 subRoot, return true if there is a subtree of root with
the same structure and node values of subRoot and
false otherwise.

A subtree of a binary tree tree is a tree that
 consists of a node in tree and all of this
node's descendants. The tree tree could also
be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

Takeaway:

The brute force algorithm will o(s *t)

But most tree problems are easier when we think recursively.

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
    
    def is_subtree_(self, root, subRoot) -> bool:
        # my first approach
        # not complete
        def same_tree(s, q): pass
        
        # both None
        if not root and not subRoot:
            return True
        
        # one of the is None
        if not root or not subRoot:
            return True
        
        pass
    
    def is_subtree(self, root, subRoot):
        # Helper function to check if two trees are the same.
        def same_tree(s, q):
            if not s and not q:
                return True
            if not s or not q:
                return False
            return s.val == q.val and same_tree(s.left, q.left) and same_tree(s.right, q.right)

        # Base case: If the current node of the root tree is None, return False.
        if not root:
            return False

        # Check if the current subtree rooted at the current node matches the subRoot tree.
        if same_tree(root, subRoot):
            return True

        # If not, recursively check the left and right subtrees of the root tree.
        return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)


    def isSubtree(self, root, subRoot) -> bool:
        
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
        
        # if bothe trees are not None and they have same values
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        
        # if one of them is empty and the othe is not
        return False

        