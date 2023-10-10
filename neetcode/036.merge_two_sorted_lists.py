"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be
made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
 
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 
Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.


Takeaway:


"""

from copy import deepcopy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_two_lists(self, list1, list2):
        # lets select one list as a baseline 

        # connect all elements of the other list based on the condition where:
        # elem1 < elem2  < elem1.next

        result_list = deepcopy(list1)

        while result_list.next.next is not None:
            if list2.next > result_list.next and list2.next < result_list.next.next:
                temp = result_list.next.next 
                result_list.next.next = list2.next

        return result_list.next

    def mergeTwoLists(self, list1, list2):
        pass

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge_two_lists(list1 = [1,2,4], list2 = [1,3,4]))
    print(sol.merge_two_lists(list1 = [], list2 = []))
    print(sol.merge_two_lists(list1 = [], list2 = [0]))

    print(sol.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
    print(sol.mergeTwoLists(list1 = [], list2 = []))
    print(sol.mergeTwoLists(list1 = [], list2 = [0]))