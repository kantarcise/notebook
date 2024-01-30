"""
You are given the root of a binary tree with unique values, and 
an integer start. 

At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

Example 1:

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:

Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.

Takeaway:

DFS combined with

max() and min(). Time and time again, we need to use it.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # from a homie
        # Initialize a instance variable to store the result
        self.ans = 0

        # Helper function to perform depth-first search
        def dfs(root, start):

            # Base case: if the current node is None, return 0 and False
            if root is None:
                return 0, False

            # Recursive calls for the left and right subtrees
            left, found_in_left = dfs(root.left, start)
            right, found_in_right = dfs(root.right, start)

            # If the current node's value is equal to the target 'start'
            if root.val == start:
                # Update the global result with the maximum of current and children's depths
                self.ans = max(self.ans, max(left, right))
                return 1, True

            # If 'start' is found in the left subtree
            if found_in_left:
                # Update the global result with the sum of left and right depths
                self.ans = max(self.ans, right + left)
                return left + 1, True

            # If 'start' is found in the right subtree
            elif found_in_right:
                # Update the global result with the sum of left and right depths
                self.ans = max(self.ans, right + left)
                return right + 1, True

            # If 'start' is not found in either subtree
            else:
                # Return the maximum depth of the left and right subtrees + 1, and False
                return max(left, right) + 1, False

        # Call the dfs function with the root and start values
        dfs(root, start)
        # Return the final result
        return self.ans
    
    def amountOfTime_(self, root: Optional[TreeNode], start: int) -> int:
        
        def traverse(node) -> int:
            left_depth = traverse(node.left) if node.left else 0
            right_depth = traverse(node.right) if node.right else 0

            if node.val == start:
                self.ans = max(left_depth, right_depth)
                return -1
            elif left_depth < 0 or right_depth < 0:
                self.ans = max(self.ans, abs(left_depth - right_depth))
                return min(left_depth, right_depth) - 1
            
            return max(left_depth, right_depth) + 1
        
        ans = 0
        traverse(root)
        return self.ans
