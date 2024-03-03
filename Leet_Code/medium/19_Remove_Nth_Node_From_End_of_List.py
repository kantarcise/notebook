"""
Given the head of a linked list, remove the nth node 
from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?

Takeaway:

  Singly Linked List training, pointers will help.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd_(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # [1,2,3,4,5]
        # 2
        # [1,2,3,5]
        # remove nth node
        node = head
        # until we see None
        while node:
            next_node = node.next
            if next_node and next_node.val == n:
                # make a new connection
                node.next = next_node.next
                # drop the node 
                next_node = None
            node = node.next
                
        return head
    
    def removeNthFromEnd__(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # DOES NOT WORK ON EDGE CASES
        # needed to add
        # if not fast: 
        #     return head.next
        
        # we got a hint
        
        # Maintain two pointers and update 
        # one with a delay of n steps.
        
        
        slow, fast = head, head
        
        for _ in range(n):
            fast = fast.next
        print("slow now", slow)
        print("fast now", fast)
        
        # before we run out on fast pointer
        while fast:
            slow = slow.next
            fast = fast.next
        # at this point, slow will be 
        # exactly what we want to remove            
        print("xx", slow)
        print("yy", fast)
        
        slow.next = slow.next.next
        slow = None
           
        return head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers, with 
        # difference of n in steps
        fast, slow = head, head
        
        # move fast
        for _ in range(n): 
            fast = fast.next
        # we encountered early end
        if not fast: 
            return head.next
        
        while fast.next: 
            fast, slow = fast.next, slow.next
        
        slow.next = slow.next.next
        
        return head
