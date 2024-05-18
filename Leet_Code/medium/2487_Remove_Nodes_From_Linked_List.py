"""
You are given the head of a linked list.

Remove every node which has a node with 
a greater value anywhere to the 
right side of it.

Return the head of the modified linked list.

Example 1:

    Input: head = [5,2,13,3,8]
    
    Output: [13,8]
    
    Explanation: 
        
        The nodes that should be removed are 5, 2 and 3.
        
        - Node 13 is to the right of node 5.
        - Node 13 is to the right of node 2.
        - Node 8 is to the right of node 3.

Example 2:

    Input: head = [1,1,1,1]
    
    Output: [1,1,1,1]
    
    Explanation: 
        Every node has value 1, so no nodes are removed.
 

Constraints:

    The number of the nodes in the given list 
        is in the range [1, 10^5].
    
    1 <= Node.val <= 10^5

Takeaway:

    Good time to use a stack!
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        cur = head
        stack = []
        # push elements onto stack
        # with a condition
        while cur:
            # stack is not empty
            # and
            # last element in the stack is 
            # smaller than current
            while stack and stack[-1].val < cur.val:
                # remove all elements smaller than current
                stack.pop()
            
            # append the element 
            stack.append(cur)

            # onto the next
            cur = cur.next
        
        # build a Linked List from stack
        # in reverse!
        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur
        
        return cur
    
sol = Solution()
result = sol.removeNodes(ListNode(5,ListNode(2,ListNode(13,ListNode(3,ListNode(8))))))

while result:
    print(result.val)
    result = result.next
