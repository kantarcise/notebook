"""
Design a class to find the kth largest element in a stream. 

Note that it is the kth largest element in the sorted order, not the 
kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with 
        the integer k and the stream of integers nums.

    int add(int val) Appends the integer val to the stream 
        and returns the element representing the kth 
        largest element in the stream.
 
Example 1:

    Input:
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    
    Output:
        [null, 4, 5, 5, 8, 8]

    Explanation:

        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        kthLargest.add(10);  // return 5
        kthLargest.add(9);   // return 8
        kthLargest.add(4);   // return 8
 
Constraints:

    1 <= k <= 10^4
    
    0 <= nums.length <= 10^4
    
    -10^4 <= nums[i] <= 10^4
    
    -10^4 <= val <= 10^4
    
    At most 10^4 calls will be made to add.
    
    It is guaranteed that there will be at least k elements 
    
    in the array when you search for the kth element.

Takeaway:

    if we use an array,
    sorting would be n log n
    finding where to insert would be o(n)

    lets use a min heap of size k
    we can get the min of min heap in o(1)
    we can add an element in log n time

    kth element will be the smallest element in 
    size k min heap
"""

from heapq import heapify, heappush, heappop


class KthLargest_:
    # THIS DOES NOT WORK
    # Nice try but yeah.

    def __init__(self, k: int, nums: "list[int]"):
        """This was an attempt to make MaxHeap
        Turns out its not needed."""
        negative_nums = [-elem for elem in nums]
        
        heapify(negative_nums)
        self.stream = negative_nums  
        self.k = k

    def add(self, val: int) -> int:
        # pushes a new item on the heap
        heappush(self.stream,  (-1) * val)
        #  return kth item on the heap without popping it
        return self.stream[self.k - 1]

class KthLargest:

    # if we use an array,
    # sorting would be n log n
    # finding where to insert would be o(n)

    # lets use a min heap of size k
    # we can get the min of min heap in o(1)
    # we can add an element in log n time
    
    def __init__(self, k: int,  nums: "list[int]"):
        # minheap with K largest integers
        self.heap = nums
        self.k = k
        # turn the list into a minimum heap
        heapify(self.heap)

        # we only need a heap with k elements
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        # if we have more elements than k
        if len(self.heap) > self.k:
            heappop(self.heap)

        # kth element is the smallest now
        return (self.heap[0])

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
