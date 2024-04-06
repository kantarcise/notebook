"""
Given the head of a linked list, remove the nth node from 
the end of the list and return its head.

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

Follow up: 

    Could you do this in one pass?

Takeaway: 

    Like a lot of LL questions, lets use two pointers

    1 2 3 4 5  n = 2  - how can we identify 4 is the 
        second to last element ?

    lets initialize left pointer at the beginning of the list
    and move right pointer n times (it will start at 3)    

    this way the space between two pointers will be exactly
    when right pointer reaches None, left pointer will be at 4

    but because we want to delete 4, we need Left pointer to be at
    so lets add a dummy node at the beginning.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def removeNthFromEnd__(self, head, n):
        # my first try
        # does not work
        length = 0
        dummy = head

        while dummy:
            length += 1
            dummy = dummy.next

        # now I know the length of the LL
        positive_count = length - n

        if positive_count == 0:
            return head.next  # Remove the first node

        index = 0
        dummy = ListNode(0)  # Make a dummy node for handling edge cases
        dummy.next = head
        current = dummy

        while current:
            if index == positive_count:
                current.next = current.next.next
                break
            index += 1
            current = current.next

        return dummy.next

    def remove_nth_from_end_(self, head, n):
        # expert advice

        # Create a dummy node to handle edge cases.
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Move the fast pointer n+1 steps ahead.
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both slow and fast pointers until the fast pointer reaches the end.
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end.
        slow.next = slow.next.next
        
        return dummy.next
    
    def removeNthFromEnd(self, head, n):

        # 1 2 3 4 5  n = 2

        # Like a lot of LL questions, lets use two pointers
        
        # how can we identify 4 is the second to last element ?

        # lets initialize left pointer at the beginning of the list
        # and move right pointer n times (it will start at 3)    
        
        # this way the space between two pointers will be exactly
        # when right pointer reaches None, left pointer will be at 4
        
        # but because we want to delete 4, we need Left pointer to be at 3

        # so lets add a dummy node at the beginning
        dummy = ListNode(0 , head)
        left = dummy 
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next

        return dummy.next

if __name__ == "__main__":
    ll1 = ListNode(1, ListNode(2, ListNode(3)))
    
    sol = Solution()
    
    modified_ll = sol.removeNthFromEnd(ll1, 1)
    while modified_ll:
        print(modified_ll.val, end=" -> ")
        modified_ll = modified_ll.next
    print("None")
