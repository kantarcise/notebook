"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

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

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

Takeaway:

Using a LL is cool. A variation of a stack so, think 
about how you can hold information on nodes.

"""

## The min value will be updated on each node - for each push and pop
# so we can hold the minimum value on the node itself.
# when the node gets deleted, head nodes min value will be used!

class Node:
    def __init__(self, value, min_val, next = None):
        self.value = value
        self.min_val = min_val
        self.next = next

class MinStack:
    """A minimum element special stack implemented with LLs"""
    def __init__(self):
        self.head = None

    def push(self, val):
        """Push the element onto stack, update min value"""
        if not self.head:
            new_node = Node(val, val)
        else:
            # if stack is occupied
            new_min = min(self.head.min_val , val)
            # make a new node pointing to the current head
            new_node = Node(val, new_min, self.head)
        self.head = new_node

    def pop(self):
        """Pop the element on top of stack
        Not returning the answer"""
        if self.head:
            self.head = self.head.next

    def top(self):
        if self.head:
            return self.head.value

    def getMin(self):
        if self.head:
            return self.head.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
