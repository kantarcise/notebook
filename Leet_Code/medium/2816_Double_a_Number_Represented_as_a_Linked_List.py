"""
You are given the head of a non-empty 
linked list representing a non-negative 
integer without leading zeroes.

Return the head of the linked 
list after doubling it.

Example 1:

    Input: head = [1,8,9]
    
    Output: [3,7,8]
    
    Explanation: Hence, the returned linked 
        list represents the number 189 * 2 = 378.

Example 2:

    Input: head = [9,9,9]
    
    Output: [1,9,9,8]
    
    Explanation: Hence, the returned linked list 
    reprersents the number 999 * 2 = 1998. 
 

Constraints:

    The number of nodes in the list is in the range [1, 104]
    
    0 <= Node.val <= 9
    
    The input is generated such that the list 
        represents a number that does not have
        leading zeros, except the number 0 itself.

Takeaway:

    Both list and two pointer approach is cool.
    
"""


from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt__(self, head: ListNode) -> ListNode:
        # did not work
        # ValueError: Exceeds the limit (4300 digits) for integer 
        # string conversion: value has 4590 digits; 
        # use sys.set_int_max_str_digits() to increase the limit
        
        # we can make a deq
        # traverse and append values on it
        # type convert,
        # make a new list from it
        q = deque()
        node = head
        while node:
            q.append(node.val)
            node = node.next
        
        number = int("".join(str(elem) for elem in q)) * 2
    
        """
        This did not work because the 
        list was reversed.
        
        # starting from leftmost digit
        # build the ll   
        new_list = ListNode(number % 10)
        new_head = new_list
        number = number // 10
        
        while number:
            digit = number % 10
            new_head.next = ListNode(digit)
            new_head = new_head.next
            number = number // 10
        
        return new_list
        """

        # convert number to string to 
        # easily get digits in reverse order
        num_str = str(number)
        
        # build the new list
        new_head = ListNode(num_str[0])
        current = new_head
        for digit in num_str[1:]:
            current.next = ListNode(digit)
            current = current.next
        
        return new_head
    
    def doubleIt_(self, head: ListNode) -> ListNode:
        # stack solution
        
        # Initialize an empty list to 
        # store the values of the linked list
        values = []
        val = 0

        # Traverse the linked list and 
        # push its values onto the list
        while head is not None:
            values.append(head.val)
            head = head.next

        print(values) # [1, 8, 9]

        new_tail = None

        # Iterate over the list of 
        # values and the carryover
        while values or val != 0:
            # make a new ListNode with value 0 and 
            # the previous tail as its next node
            new_tail = ListNode(0, new_tail)

            # Calculate the new value for 
            # the current node
            # by doubling the last digit, adding 
            # carry, and getting the remainder
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10

        # Return the tail of the new linked list
        return new_tail
    
    def doubleIt(self, head: ListNode) -> ListNode:
        # two pointers
        
        curr = head
        prev = None

        # Traverse the linked list
        while curr:
            twice_of_val = curr.val * 2

            # If the doubled value is less than 10
            if twice_of_val < 10:
                curr.val = twice_of_val
            # If doubled value is 10 or greater
            elif prev:  # other than first node
                # Update current node's value with 
                # units digit of the doubled value
                curr.val = twice_of_val % 10
                # Add the carry to the previous node's value
                prev.val += 1
            else:  # first node
                # make a new node with carry as value 
                # and link it to the current node
                head = ListNode(1, curr)
                # Update current node's value with units 
                # digit of the doubled value
                curr.val = twice_of_val % 10

            # Update prev and curr pointers
            prev = curr
            curr = curr.next

        return head
    
sol = Solution()
result = sol.doubleIt_(ListNode(1,ListNode(8,ListNode(9))))

while result:
    print(result.val)
    result = result.next
