"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal 
queue (push, peek, pop, and empty).

Implement the MyQueue class:

  void push(int x) Pushes element x to the back of the queue.
  int pop() Removes the element from the front of the queue and returns it.
  int peek() Returns the element at the front of the queue.
  boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

You must use only standard operations of a stack, which means only 
push to top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, the stack may not be supported natively. You may 
simulate a stack using a list or deque (double-ended queue) as long as you use 
only a stack's standard operations.
 
Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Takeaway:

We have to move around the stacks to emulate queues.
"""

class MyQueue:
    """a queue
    [1,2,3]
    [1,2,3,4]
    [2,3,4]
    lets use one stack for adding items.
    other for reversing order.
    """
    
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        # push to the end
        self.stack_one.append(x)
        
    def pop(self) -> int:
        # pop from beginning, fifo
        # if we are going to pop a value, we 
        # need to reverse order
        self.move()
        return self.stack_two.pop()

    def peek(self) -> int:
        # we want to look at the FIFO of the queue
        self.move()
        return self.stack_two[-1]

    def empty(self) -> bool:
        return not self.stack_one and not self.stack_two
    
    def move(self):
        # if stack two is not empty 
        # do not do anything
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
