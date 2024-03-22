"""
Given the head of a singly linked list, reverse the 
list, and return the reversed list.
 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

  The number of nodes in the list is the range [0, 5000].
  -5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either 
iteratively or recursively. Could you implement both?

Takeaway:

  YEAH cool but, can you reverse a linked list?

"""

from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # store all values in a deque
        all_values = deque()
        start = head
        while start:
            all_values.append(start.val)
            start = start.next
        
        # make initial node
        reverse_head = ListNode(all_values.pop())
        current = reverse_head

        # construct reverse
        while all_values:
            temp = ListNode(all_values.pop())
            current.next = temp
            current = temp

        return reverse_head

    def reverseList_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # another approach - simple and easy
        
        # the list looks like 1 - 2 - 3
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the pointer
            
            prev = current            # Move prev to the current node
            current = next_node       # Move current to the saved next node
        
        return prev
