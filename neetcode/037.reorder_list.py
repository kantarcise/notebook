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

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000

Takeaway:

    Two phases:

    Find second portion of the linked list, reverse it
    add it one by one

    To find the middle of the LL, use a slow and fast pointer

    slow pointer at first node, fast pointer at second node

    keep going until fast pointer reaches None or last element

    if it is an even list, slow pointer will be the 
    last element of the first portion

    if it is an odd list slow pointer will 
    be in the middle exactly

    we need pointer at the beginning of each first and second lists

    for the last node of the first list, node.next should be None 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reorderList__(self, head) -> None:
        # my first attempt   
        # not working correctly 
        
        # [1,2,3,4,5] 
        # [1,5,2,4,3]
        traverse = head.next

        while traverse:
            # store the next value
            temp = traverse.next
            traverse.next = 5

            traverse = traverse.next
            traverse.next = temp

        return head
    
    def reorderList_(self, head):
        
        if not head or not head.next:
            return head

        # Find the middle of the linked list using the slow and fast pointer technique.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list.
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the two halves of the linked list.
        first_half, second_half = head, prev
        while second_half.next:
            next_first = first_half.next
            next_second = second_half.next
            first_half.next = second_half
            second_half.next = next_first
            first_half = next_first
            second_half = next_second

        return head

    def reorderList(self, head) -> None:

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


if __name__ == "__main__":
    # these will not work

    # sol = Solution()
    # print(sol.reorderList_(head = [1,2,3,4]))
    # print(sol.reorderList_(head = [1,2,3,4,5]))

    # print(sol.reorderList(head = [1,2,3,4]))
    # print(sol.reorderList(head = [1,2,3,4,5]))
    pass
