"""
Given the root of a binary search tree, and an 
integer k, return the kth smallest value (1-indexed) of all 
the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert 
and delete operations) and you need to find the kth smallest 
frequently, how would you optimize?

Takeaway:

We can make a recursive in order traversal and
append all elements from smallest to kth smallest 
on a temporary list

OR

lets use a stack and solve the question iteratively
this is also in order traversal

make a stack
add every node onto the stack until you get to 
where node.left is None
when you get that case, that is your leftmost element.
pop it from the stack, check if it has a node.right
than go one level up

when stack is empty, return
number of elements visited
once this is equal to k, return

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallest(self, root, k) -> int:
        # first try
        # we can do a in order traversal to get every element of the 
        # nodes in a list
        # we will have a sorted list
        # we can return the kth value 

        temp = []         
        def dfs(root):        
            if not root:
                return   
            # go to left subtree until we find a single node         
            dfs(root.left)
            if len(temp) == k:
                return
            temp.append(root.val)            
            dfs(root.right)
        dfs(root)

        # last element of temp is the node we want
        return temp[-1]

    def kthSmallest(self, root, k) -> int:
        # lets use a stack and solve the question iteratively
        # this is also in order traversal

        # make a stack
        # add every node onto the stack until you get to 
        # where node.left is None
        # when you get that case, that is your leftmost element.
        # pop it from the stack, check if it has a node.right
        # than go one level up

        # when stack is empty, return
        
        # number of elements visited
        # once this is equal to k, return
        n = 0
        stack = []

        current = root
        # while current is not None and stack is not empty
        while current or stack:
            while current:
                
                stack.append(current)
                current = current.left

            # current is None
            current = stack.pop()
            # we visited a node
            n += 1

            if n == k:
                return current.val
            
            # check the right subtree
            current = current.right