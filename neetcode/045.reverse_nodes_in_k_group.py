"""
Given the head of a linked list, reverse the nodes
of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal
to the length of the linked list. 

If the number of nodes is not a multiple of k then 
left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's
nodes, only nodes themselves may be changed.

Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:

    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
 
Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
 
Follow-up: 
    Can you solve the problem in O(1) extra memory space?

Takeaway:

    Start with a dummy node and sets it as the
     previous node for the first group. 
     This dummy node simplifies the code for handling
    the head of the list and avoids edge cases.

    You can write a simple helper function to get the kth node

    It then identifies the next group by accessing
    the node immediately following the kth node.

    The core part of the code is the loop that reverses
     the k nodes in the current group. It uses two
    pointers (prev and current) to reverse the direction
    of the next pointers for the k nodes.
    This effectively reverses the group.

    After reversing the group, it updates the pointers to link 
    the reversed group to the previous group. It also sets
     group_prev to the previous group's end, which prepares
    it for the next iteration.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head, k):
        # neet
        
        # Make a dummy node and set it as the previous 
        # node for the first group
        dummy = ListNode(0 , head)
        group_prev = dummy

        while True:
            # Get the kth node in the current group
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            # two pointers
            prev, current = kth.next, group_prev.next
            while current != group_next:
                # hold the next value
                temp = current.next
                # turn the pointer 180
                current.next = prev
                # move to the next
                prev = current
                current = temp
            
            # Update the pointers to link the reversed
            #  group to the previous group
            temporary = group_prev.next
            group_prev.next = kth
            group_prev = temporary

        return dummy.next
    
    def get_kth_node(self, current, k):
        while current and k > 0 :
            current = current.next
            k -= 1
        return current

    
    def reverseKGroupRecursive(self, head, k):
        # expert advice

        # Check if there are at least k nodes remaining
        if not self.has_k_nodes(head, k):
            return head

        # Initialize the pointers for reversing
        prev, curr, next_node = None, head, None
        count = 0

        # Reverse the first k nodes
        while count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # Recursively reverse the next group and connect it to the current group
        head.next = self.reverseKGroupRecursive(curr, k)

        # 'prev' is now the new head of the group
        return prev

    # Helper function to check if there are at least k nodes remaining
    def has_k_nodes(self, head, k):
        count = 0
        while head:
            count += 1
            if count >= k:
                return True
            head = head.next
        return False
