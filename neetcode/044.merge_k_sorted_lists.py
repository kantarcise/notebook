"""
You are given an array of k linked-lists lists, each 
linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted 
linked-list and return it.

Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Explanation: 
    
        The linked-lists are:
            [
              1->4->5,
              1->3->4,
              2->6
            ]

        merging them into one sorted list:
        1->1->2->3->4->4->5->6

Example 2:

    Input: lists = []
    Output: []

Example 3:

    Input: lists = [[]]
    Output: []
 
Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.

Takeaway:

    My initial solution was to use a simple list and 
    get every element in it, sort it and make a new LL

    The problem is about Merge Sort
    simply merge two lists until you have merged them all.

    ** do not forget edge cases ** 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists_(self, lists):
        # this is MY approach
        # just use a list and sort it to make a new list
        
        result = ListNode()
        all_values = []

        for single_list in lists:
            while single_list:
                all_values.append(single_list.val)
                single_list = single_list.next 
        
        all_values.sort()
        
        # first node will be just empty
        current = result

        for elem in all_values:
            # make a new node on Next
            current.next = ListNode(elem)
            # move forward
            current = current.next

        # return from the next of the empty node
        return result.next
        
    def mergeKLists(self, lists):
        # this is actually about merge sort    
        
        # instead of adding a new node for a LL and each time 
        # comparing all of the existing Nodes within
        # we can use merge sort, so merge 2 by 2 and merge 2s together
        
        # edge cases
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            # iterate through each list
            # we are going to merge them two by two
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # l2 could be None, so check it
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # merge these lists and append them to the merged_lists
                merged_lists.append(self.mergeList(l1, l2))
            
            # update the lists variable
            lists = merged_lists

        # in the end there will be only one list left
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # move to the next node in the result
            tail = tail.next

        # edge case,
        # if they are not equal in size, add them to the end.
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
