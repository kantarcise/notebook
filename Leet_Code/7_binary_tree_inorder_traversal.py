# If you encounter a problem like this, you can simply look at the example or search the internet about what it is that trying to be achieved.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # To remember the traversal:  https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        my_list = []
        self.arrange(root, my_list)
        return my_list

    def arrange(self, root, my_second_list):
        if (root == None):
            return 
        # If there is a element on the left, we will append it on the list
        self.arrange(root.left, my_second_list)
        # If no element on the left, we append the root
        my_second_list.append(root.val)
        # Lastly we append the right element if exists.
        self.arrange(root.right, my_second_list)
