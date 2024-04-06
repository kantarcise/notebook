"""
Design a data structure that follows the constraints 
of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with
        positive size capacity.

    int get(int key) Return the value of the key if the 
        key exists, otherwise return -1.

    void put(int key, int value) Update the value of 
        the key if the key exists. Otherwise, add the
        key-value pair to the cache. If the number of keys 
        exceeds the capacity from this operation, evict
        the least recently used key.

The functions get and put must each run in O(1) 
average time complexity.

Example 1:

    Input
    ["LRUCache", "put", "put", "get", "put", 
            "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], 
            [2], [4, 4], [1], [3], [4]]

    Output
    
        [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    
        LRUCache lRUCache = new LRUCache(2);

        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1);    // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, 
                                    cache is {1=1, 3=3}

        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, 
                                    cache is {4=4, 3=3}

        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4
 
Constraints:

    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.

Takeaway:

    We will have a capacity

    we will have a doubly linked list, also a hash map
    with keys and values as pointers to nodes.

    LRU and most recent will be pointed and updated.
    So we need two pointers just for those. Which will be Nodes as well.

    You can also use Queues, implemented with Python lists

"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    """
    A class for Least Recently Used (LRU) data structure.
    
    Example:
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map the key to nodes, the hashmap
        self.cache = {}

        # kinda like header and trailer sentinel nodes
        self.left , self.right = Node(0, 0), Node(0 , 0)
        
        # left is Least Recently Used, Right is Most Recently Used
        # make connections
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # remove the node from LL
        
        temp_prev = node.prev
        temp_next = node.next

        temp_prev.next = temp_next
        temp_next.prev = temp_prev
        
        pass

    def insert(self, node):
        # insert node at right of LL 
        # right before the right pointer
        
        # the nodes 
        temp_prev = self.right.prev
        temp_next = self.right

        # node is inserted
        temp_prev.next = node
        temp_next.prev = node

        # node's pointers
        node.prev = temp_prev
        node.next = self.right        


    def get(self, key: int) -> int:
        if key in self.cache:
            # move the node at the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # return the value of the node
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the old one and add the new
            self.remove(self.cache[key])
        
        # make a new node
        self.cache[key] = Node(key, value)
        # add the node to LL
        self.insert(self.cache[key])            
        
        
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


"""
Here is something extra

Not ideal, queue with list. popping from beginning
"""

from collections import deque

class LRUCacheWithQueue:
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.queue.pop(self.queue.index(key))
        self.queue.append(key)
        # self.check()
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if len(self.queue) < self.capacity and key not in self.queue:
            self.queue.append(key)
            self.check()
            return
        if key in self.queue:
            # move to end
            self.queue.pop(self.queue.index(key))
        else:
            old_key = self.queue.pop(0)
            print(f"Popping old key={old_key}")
            self.cache.pop(old_key)
        self.queue.append(key)
        # self.check()
    
    def __repr__(self):
        return f"queue = {self.queue}, cache={self.cache}"

    def check(self):
        if len(self.queue) != len(self.cache):
            print("ERROR")
            print(str(self))
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
