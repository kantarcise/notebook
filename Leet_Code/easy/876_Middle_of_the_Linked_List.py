"""
Given the head of a singly linked list, return 
the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes 
with values 3 and 4, we return the second one.
 

Constraints:

  The number of nodes in the list is in the range [1, 100].
  1 <= Node.val <= 100

Takeaway:

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tortoise and hare
        # we do not need a counter
            
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def middleNode_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # works but slower
        # get the length of LL
      
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        # move half of length times
        result = head
        for _ in range(length//2):
            result = result.next
            
        return result
