"""
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or 
memory buffer, or transmitted across a network connection link to 
be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 

There is no restriction on how your serialization/deserialization algorithm 
should work. 

You just need to ensure that a binary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode 
serializes a binary tree. You do not necessarily need to follow 
this format, so please be creative and come up with different 
approaches yourself.

Example 1:

    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Example 2:

    Input: root = []
    Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000

Takeaway:

    You can solve the problem with breadth-first search
    or you can solve it with depth first search
    using preorder traversal

    for the example tree
         1
        / \
       2   3
          / \
         4   5

    "1,2,N,N,3,4,N,N,5,N,N"
    is the resulting string
    if we used N for None nodes

    For each subtree, check the left and right nodes,
    and recursively go a level up

    Also added the Breadth First Search Solution

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SezaiCodec:
    # I TRIED REALLY HARD, BUT THIS WAS NOT ACCEPPTED.


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # if root is None 
        if not root:
            return ""

        # lets use depth-first search
        # and implement the tree using an array 
        # return the string of the array after.
        # * nodes are for the none nodes
        tree_as_array = []

        def dfs(node):
            if not node:
                tree_as_array.append("*")
                return
            
            tree_as_array.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ",".join(tree_as_array)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if no data, return None 
        if not data:
            return None

        nodes = data.split(",")

        def inverse_dfs(nodes_list):

            if not nodes_list:
                return None

            root = TreeNode(nodes_list[0])
            for i in range(1,len(nodes_list) - 1):
                if nodes_list[i] == "*":
                    return
                if i % 2 == 0:
                    root.left = inverse_dfs(nodes_list[i + 1:])
                if i % 2 == 1:
                    root.right = inverse_dfs(nodes_list[i + 1:])
            return root

        tree = inverse_dfs(nodes)

        return tree
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:

    # You can solve the problem with breadth-first search
    # or you can solve it with depth first search
    # using preorder traversal

    # for the example tree
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5

    # "1,2,N,N,3,4,N,N,5,N,N"
    # is the resulting string
    # if we used N for None nodes

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        result = []
        # preorder depth-first search
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes_list = data.split(",")
        self.i = 0

        def dfs():
            if nodes_list[self.i] == "N":
                # onto the next element
                self.i += 1
                # return a None node
                return None
            node = TreeNode(int(nodes_list[self.i]))
            self.i += 1
            # construct the left subtree
            node.left = dfs()
            # construct the right subtree
            node.right = dfs()
            return node
        
        return dfs()

from collections import deque

class CodecSecond:
    # Breadth-first Search Solution

    def serialize(self, root):
        if root == None: 
            # let "#" be None node
            return "#"
        
        # Start by making a deque
        bfs = deque([root])
        ans = []
        while bfs:
            curr = bfs.popleft()
            if curr == None:
                ans.append("#")
            else:
                ans.append(str(curr.val))
                bfs.append(curr.left)
                bfs.append(curr.right)
        return ",".join(ans)

    def deserialize(self, data):
        def make_node(str_value):
            if str_value == "#":
                return None
            return TreeNode(int(str_value))

        if data == "#": 
            return None
        
        node_list = data.split(",")
        root = make_node(node_list[0])
        i = 1
        bfs = deque([root])
        while bfs:
            curr = bfs.popleft()
            # left node
            curr.left = make_node(node_list[i])
            # right node
            curr.right = make_node(node_list[i+1])
            # move counter 2 
            i += 2

            if curr.left != None:
                bfs.append(curr.left)
            if curr.right != None:
                bfs.append(curr.right)

        return root

if __name__ == "__main__":
    # Make a binary tree:
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Make a Codec instance
    codec = Codec()

    # Serialize the tree
    serialized_tree = codec.serialize(root)
    print("Serialized Tree:", serialized_tree)  
    # Output: "1,2,*,*,3,4,*,*,5,*,*"

    # Deserialize the tree
    deserialized_tree = codec.deserialize(serialized_tree)

    # Check if the deserialized tree is the same as the original tree
    def are_trees_equal(node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (not node1 and node2):
            return False
        return (
            node1.val == node2.val
            and are_trees_equal(node1.left, node2.left)
            and are_trees_equal(node1.right, node2.right)
        )

    print("Are Trees Equal:", are_trees_equal(root, deserialized_tree))  # Output: True
