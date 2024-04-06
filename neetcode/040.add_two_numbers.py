"""
You are given two non-empty linked lists representing two 
non-negative integers. 

The digits are stored in reverse order, and each of their 
nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.

Example 1:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Takeaway:

    I was stuck in thinking the inequality of sizes for LL's. Turns out you can 
    just add 0 nodes to the one that is missing.

    My approch would work, but its not why the question is asked.

    Do not forget about trying to understand the question. Calm in the first 3 minutes.

    we check if the node is None for traversing the LinkedList.

    In addition, we have a simple condition for the sum called "CARRY"

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers_(self, l1, l2):
        # my first approach
        
        # Input: l1 = [2,4,3], l2 = [5,6,4]
        # Output: [7,0,8]
        # Explanation: 342 + 465 = 807.
        
        # for both of the LL's we can traverse them and hold a string for each
        # then find the result for those strings with int conversion 
        # and make a new list.
        
        # 123
        #   3
        # ---
        # 126

        # i think this will work, but its not why the question is asked.

        pass

    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        # if the size is different for two linked lists. you just add a node with 0
        # there is a carry for results over 10 for the addition

        # if carry is not None, continue iterating
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit 
            val = v1 + v2 + carry

            # after calculation
            # new carry
            carry = val // 10
            # new value
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            # if there are still nodes avaliable, go to them.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # what if the last summation is 8 + 7
        # there has to be one more carry for it. 
        return dummy.next

if __name__ == '__main__':

    # cannot really make it work
    
    # sol = Solution()
    # print(sol.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
    # print(sol.addTwoNumbers(l1 = [0], l2 = [0]))
    # print(sol.addTwoNumbers( l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))
    pass
