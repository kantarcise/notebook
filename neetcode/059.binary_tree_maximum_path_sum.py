"""
A path in a binary tree is a sequence of nodes where each pair of 
adjacent nodes in the sequence has an edge connecting them. A node 
can only appear in the sequence at most once. Note that the path 
does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000

Takeaway:

negative values can be included in a max path
just think -1

to make a path, we need to choose between 2 options.
we cannot go everywhere like a euler tour
        
we will use dfs and starting from subtrees
we will return the maximum value to parent 
without splitting    

an edge case is for negative valued children
we can choose not to include the children by using
max(left, right, 0)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # DOES NOT WORK
    def maxPathSum(self, root: "TreeNode") -> int:        
        # THIS DOESNT WORK
        
        # we can clearly see that we do not want to 
        # add negative values in our path

        # if possible, we would like to have the longest path
        # that consists of positive values

        # but a shorter path can have a bigger sum

        # i guess we can use dfs to gather all possible paths,
        # and return the one with the max

        path = []
        current_max = float("-inf")

        def dfs(node):
            nonlocal current_max
        
            if not node:
                return
            
            if node.val > 0:
                path.append(node.val)
                current_path_sum = sum(path)
                current_max = max(current_max, current_path_sum)  # Update current_max if needed

            else:
                current_max = max(current_max, sum(path))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return current_max

    # DOES NOT WORK
    def max_path_sum_neetcode(self, root: "TreeNode") -> int:
        # Actually, negative values can be included in a max path
        # just think -1

        # to make a path, we need to choose between 2 options.
        # we cannot go everywhere like a euler tour
        
        # we will use dfs and starting from subtrees
        # we will return the maximum value to parent 
        # without splitting    

        # an edge case is for negative valued children
        # we can choose not to include the children by using
        # max(left, right, 0)

        # THIS SOLUTION: MAXIMUM RECURSION DEPTH EXCEEDED

        result = [root.val]

        def dfs(node):
            # no root
            if not node:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute max path sum WITH split
            #        3
            #      4   5
            result[0] = max(result[0], root.val + left_max + right_max) 

            # give one level up the result WITHOUT splitting
            return root.val + max(left_max, right_max)

        dfs(root)

        return result[0]

    # DOES WORK
    def __init__(self):
        self.globalmax = float('-inf')

    def maxPathSum(self, root):
        self.findmax(root)
        return self.globalmax

    def findmax(self, node):
        # a depth first search
        if not node:
            return 0
        # get the left and right nodes
        left = self.findmax(node.left)
        right = self.findmax(node.right)

        # if it is negative, do not choose to append it
        if left < 0: left = 0
        if right < 0: right = 0

        # this is the current max within the current subtree
        #   3
        #  4 5
        self.globalmax = max(left + right + node.val, self.globalmax)
        
        # return the path without splitting to one level above
        return max(left, right) + node.val