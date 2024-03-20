"""
You are given two linked lists: list1 and list2 of 
sizes n and m respectively.

Remove list1's nodes from the ath node to 
the bth node, and put list2 in their place.

The blue edges and nodes in the 
following figure indicate the result:

Build the result list and return its head.

Example 1:

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, 
        list2 = [1000000,1000001,1000002]

Output: [10,1,13,1000000,1000001,1000002,5]

Explanation: We remove the nodes 3 and 4 and put the 
      entire list2 in their place. The blue edges and 
      nodes in the above figure indicate the result.

Example 2:

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, 
      list2 = [1000000,1000001,1000002,1000003,1000004]

Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]

Explanation: Same logic.

Constraints:

  3 <= list1.length <= 10^4
  1 <= a <= b < list1.length - 1
  1 <= list2.length <= 10^4

Takeaway:

  Simply, understand the question before you attempt it.
  Traversals until conditions met.
  
  Identifiers are aliases.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween_(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # this is what happens if you do not understand the question
        
        # you solve the wrong one
        
        # we need to find the value just before a
        # we need to break the next from b
        # we need to attach a-1.next to new list head
        # we need to attach new list last node next to b+1
        
        # find beginning
        a_prev, a_current = list1, list1
        
        while a_current.val != a:
            a_prev = a_prev.next
            a_current = a_current.next  
            
        # find the end
        b_prev, b_current = list1, list1
        
        while b_current != b:
            b_prev = b_prev.next
            b_current = b_current.next
            
        # remove
        del a_prev.next
        del b.next
        
        a_prev.next = list2
        
        end_of_l2 = list2
        
        while end_of_l2:
            end_of_l2 = end_of_l2.next
            
        end_of_l2.next = b_current
        
        return list1
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # this works
        # a'th node to b'th node
        
        step = 0
        start_prev, start_current = list1, list1.next
        
        while step < a - 1:
            start_prev = start_prev.next
            start_current = start_current.next
            step += 1
            
        end_prev, end_current = list1, list1.next
        
        count = 0 
        while count < b:
            end_prev = end_prev.next
            end_current = end_current.next
            count += 1
        
        # find end of list2
        starting, ending = list2, list2
        while ending.next:
            ending = ending.next
        
        # when in doubt, print all the lists
        
        # print(start_prev)
        # print(start_current)
        # print("-")
        # print(end_prev)
        # print(end_current)
        # print(starting)
        # print(ending)
        
        start_prev.next = starting
        # if not b < len(list1)
        # del end_prev.next
        ending.next = end_current
        
        return list1
        
    def mergeInBetween__(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # simpler code here, works
        
        # Find the ath node
        current = list1
        for _ in range(a - 1):
            current = current.next
        
        # Find the bth node
        temp = current
        for _ in range(b - a + 2):
            temp = temp.next
        
        # Connect ath node to the head of list2
        current.next = list2
        
        # Find the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the end of list2 to the b+1th node
        list2.next = temp
        
        return list1
