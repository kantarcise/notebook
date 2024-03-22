"""
Given the head of a singly linked list, return true 
if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

  The number of nodes in the list is in the range [1, 10^5].
  0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?

Takeaway:

  Always use placeholders (pointers).

  Tuple unpacking is cool.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome_(self, head: Optional[ListNode]) -> bool:
        # brute force
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
            
        return values == values[::-1]
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # can we solve it with just O(1) space?
        
        # with tortoise and hare, it is possible!
        reverse = None
        slow = fast = head

        # Reverse the first half of the list
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
            
        # if the list is odd number of nodes then 
        # advance slow to the next node.
        if fast:
            slow = slow.next
        
        # check palindrome

        # Compare the reversed first half with 
        # the second half list.
        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next

        return not reverse
        
