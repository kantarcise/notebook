"""
Given head, the head of a linked list, determine if the 
linked list has a cycle in it.

There is a cycle in a linked list if there is some node in 
the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected 
to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. 

Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where 
the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where 
the tail connects to the 0th node.


Example 3:

Input: head = [1], pos = -1
Output: false

Explanation: There is no cycle in the linked list.

Constraints:

  The number of the nodes in the list is in the range [0, 10^4].
  -10^5 <= Node.val <= 10^5
  pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Takeaway:

Tortoise and Hare!

If you are going to setup a while loop, make sure that 

1) YOu can exit it
2) you do not run into an Error in traversal

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if there is a cycle in the ll
        # you will not ever see next == None
        
        # and two nodes will have the same next
        
        # we can use tortoise and hare
        # if they never meet there is no cycle
        
        slow, fast = head, head
        
        # we should check for both fast and
        # fast.next to avoid AttributeError
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
