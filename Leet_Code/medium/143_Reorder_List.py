"""
You are given the head of a singly linked-list. 
The list can be represented as:

  L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

  L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

  The number of nodes in the list is in the range [1, 5 * 10^4].
  1 <= Node.val <= 1000

Takeaway:

  The deque approach is solid. Or you gotta use tortoise/hare.

"""

from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # just brute force - deque
        
        # edge cases
        if not head or not head.next:
            return
        
        # Store the nodes in a deque
        nodes = deque()
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Reorder the nodes
        head = nodes.popleft()
        current = head
        while nodes:
            right = nodes.pop() # Get the last node
            current.next = right
            current = current.next
            
            if nodes: # Check if there are nodes left
                left = nodes.popleft() # Get the first node
                current.next = left
                current = current.next
              
        # Set the next of the last node to None  
        current.next = None 
        
    def reorderList_(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        # two phases
        # second portion of the linked list, reverse it
        # add it one by one
        
        # to find the middle of the LL
        # use a slow and fast pointer
        # slow pointer at first node, fast pointer at second node
        # keep going until fast pointer reaches None or last element

        # if it is an even list, slow pointer will be the 
        # last element of the first portion
        # 
        # if it is an odd list slow pointer will 
        # be in the middle exactly
        
        # we need pointer at the beginning of each first and second lists

        # for the last node of the first list, node.next should be None 
        """
        
        # find the middle of the LL
        slow, fast = head , head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now the slow is middle

        # beginning of the second half is next of slow

        second = slow.next
        # split the list
        prev = None 
        slow.next = None

        # reverse second list
        while second:
            # hold the value
            temp = second.next
            # change direction
            second.next = prev
            prev = second
            # shift
            second = temp

        # after this traverse, second will be None
        # previous will be last node what we looked at
        
        # merge two halfs
        first, second = head, prev

        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
