"""
Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 
Constraints:

    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always 
        be called on non-empty stacks.
    At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Takeaway:

    - The key takeaway from this code is that by maintaining 
    an auxiliary data structure specifically designed to 
    handle the minimum value, you can achieve O(1) time
    
    - complexity for the getMin() operation while still 
    supporting standard stack operations.
    
    - The choice between array-based and linked-list-based 
    approaches depends on your preference and specific use case.
    
    - lists has append, push, pop methods. As usual.

"""

# main Idea behind this question is that, when you want to compare values in a sequence,
# you can use a non public sequence which is specific to the thing you want to compare


"""You can use an array based sequence"""
class MinStack:

    def __init__(self):
        self._data = []
        self._min_stack = [] # to hold the current min in the stack

    def push(self, val: int) -> None:
        # add new value
        self._data.append(val)
        # check if the val is eligable for min stack
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)        

    def pop(self) -> None:
        # if the top of the stack is the min element
        if self._data[-1] == self._min_stack[-1]:
            # that min element is no longer within the main stack
            # so we have to pop it from min_stack as well
            self._min_stack.pop()
        self._data.pop()
        
    def top(self) -> int:
        return self._data[-1]
        
    def getMin(self) -> int:
        return self._min_stack[-1]


"""Or you can use Linked Based Sequence"""
class Node:
    def __init__(self, value, min_value, next_node=None):
        self.value = value
        self.min_value = min_value
        self.next = next_node

class MinStackLL:
    def __init__(self):
        self.head = None
    
    def push(self, val: int) -> None:
        # if the stack is empty,
        if self.head is None:
            new_node = Node(val, val)
        else:
            # find the new minimum value
            new_min = min(val, self.head.min_value)
            new_node = Node(val, new_min, self.head)
        self.head = new_node
    
    def pop(self) -> None:
        if self.head is not None:
            # move the head node to the next
            self.head = self.head.next
    
    def top(self) -> int:
        if self.head is not None:
            # head node is the top of the stack
            # because as we pushed values in, we moved head.
            return self.head.value
    
    def getMin(self) -> int:
        if self.head is not None:
            # head node holds the min value.
            return self.head.min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
    
if __name__ == '__main__':
    
    print("Array approach")
    
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())

    print("LL Approach")

    linked = MinStackLL()
    linked.push(-2)
    linked.push(0)
    linked.push(-3)
    print(linked.getMin())
    print(linked.pop())
    print(linked.top())
    print(linked.getMin())
