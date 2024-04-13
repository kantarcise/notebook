"""
The median is the middle value in an ordered integer list. 

If the size of the list is even, there is no middle value, and the 
median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.

For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    - MedianFinder() initializes the MedianFinder object.

    - void addNum(int num) adds the integer num from the data stream 
        to the data structure.

    - double findMedian() returns the median of all elements so far. 

    Answers within 10-5 of the actual answer will be accepted.

Example 1:

    Input:
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
    
    Output:
        [null, null, null, 1.5, null, 2.0]

    Explaination:
        
        MedianFinder medianFinder = new MedianFinder();
        medianFinder.addNum(1);    // arr = [1]
        medianFinder.addNum(2);    // arr = [1, 2]
        medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        medianFinder.addNum(3);    // arr[1, 2, 3]
        medianFinder.findMedian(); // return 2.0
 
Constraints:

    -10^5 <= num <= 10^5

    There will be at least one element in the data structure 
        before calling findMedian.
    
    At most 5 * 104 calls will be made to addNum and findMedian.
 
Follow up:

    If all integer numbers from the stream are in the range [0, 100], 
        how would you optimize your solution?

    If 99% of all integer numbers from the stream are in the 
        range [0, 100], how would you optimize your solution?

Takeaway:

    Of course first approach woul be using a list.

    The idea is basically to use two heaps a small and a large heap
    Adding and removing elements from the heap will be o(logn)

    Finding the max / min in constant time - o(1)

    small heap will be a max heap, 
    large heap will be a min heap

    Size of the heaps should be approximately Equal
    AT MOST difference of 1.

    Also, every element in small heap 
    should be smaller than the big heap

"""

from heapq import heapify, heappop, heappush, heappushpop

class MedianFinderObvious:
    # Yeah

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        # size 5
        # 0, 1, 2, 3, 4
        size = len(self.stream)
        self.stream.sort()
        if size % 2 == 0:
            return (self.stream[(size//2)] + self.stream[(size//2) - 1]) / 2
        else:
            return self.stream[size//2]


class MedianFinder:

    def __init__(self):
        # two heaps, small and large
        # small is the max heap and large is the minheap
        self.small , self.large = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        
        # make sure every elem in small is <= than every elem in large
        # small heap is max heap so root is biggest
        # large heap is min heap so root is smallest 
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        # check the size difference is only 1 or 0
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        # odd number of elems
        if len(self.small)  > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]

        # even number of elements
        # same sizes in small an large
        return ( - 1 * self.small[0] + self.large[0]) / 2
        

class MedianFinderFaster:
    # even faster
    # for the curious minds

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, num))
        else:
            heappush(self.large, -heappushpop(self.small, -num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(-self.small[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
