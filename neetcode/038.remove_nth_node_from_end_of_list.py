"""
Given the head of a linked list, remove the nth node from the end of
 the list and return its head.

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



"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def remove_nth_from_end(self, head, n):
        pass
    
    def removeNthFromEnd(self, head , n):
        pass


if __name__ == "__main__":
    
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    
    sol = Solution()        